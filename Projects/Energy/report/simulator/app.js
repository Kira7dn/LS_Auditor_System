const DATA_PATHS = {
  params: [
    "../data/calculation_parameters.json",
    "/data/calculation_parameters.json",
    "./data/calculation_parameters.json",
  ],
  pv: [
    "../data/ninja_pv_21.0158_106.8009_uncorrected.raw.json",
    "/data/ninja_pv_21.0158_106.8009_uncorrected.raw.json",
    "./data/ninja_pv_21.0158_106.8009_uncorrected.raw.json",
  ],
  wind: [
    "../data/ninja_wind_21.0158_106.8009_uncorrected.raw.json",
    "/data/ninja_wind_21.0158_106.8009_uncorrected.raw.json",
    "./data/ninja_wind_21.0158_106.8009_uncorrected.raw.json",
  ],
};

const STORAGE_KEY = "letron-energy-simulator:v2";

const inputIds = [
  "camcCount",
  "camcKm",
  "camcKwhKm",
  "camcDiesel",
  "farizonCount",
  "farizonKm",
  "farizonKwhKm",
  "farizonDiesel",
  "solarMw",
  "windKw",
  "rmfcKw",
  "rmfcDispatch",
  "rmfcEff",
  "vfbPowerMw",
  "vfbCapacityMwh",
  "vfbEff",
  "bessPowerMw",
  "bessCapacityMwh",
  "bessEff",
  "chargeEff",
  "transmissionLoss",
];

const state = {
  source: null,
  pv: null,
  wind: null,
  defaults: null,
  charts: {},
};

const els = {};
for (const id of inputIds) {
  els[id] = document.getElementById(id);
}

const kpiEls = {
  load: document.getElementById("kpiLoad"),
  renewable: document.getElementById("kpiRenewable"),
  grid: document.getElementById("kpiGrid"),
  rmfc: document.getElementById("kpiRmfc"),
  surplus: document.getElementById("kpiSurplus"),
  baseline: document.getElementById("kpiBaseline"),
  project: document.getElementById("kpiProject"),
  reduction: document.getElementById("kpiReduction"),
  reductionRate: document.getElementById("kpiReductionRate"),
  pvCf: document.getElementById("tracePvCf"),
  windCf: document.getElementById("traceWindCf"),
  storageCharge: document.getElementById("traceStorageCharge"),
  storageDischarge: document.getElementById("traceStorageDischarge"),
  storageLoss: document.getElementById("traceStorageLoss"),
  transmissionLoss: document.getElementById("traceTransmissionLoss"),
  rmfcStatus: document.getElementById("rmfcStatus"),
  dataStatus: document.getElementById("dataStatus"),
};

const monthSelect = document.getElementById("monthSelect");
const periodSelect = document.getElementById("periodSelect");

const colors = {
  solar: "#d99a2b",
  wind: "#168c91",
  rmfc: "#6c7a2f",
  storage: "#3269b1",
  grid: "#b94d4a",
  baseline: "#b94d4a",
  project: "#2f8f5b",
  surplus: "#91b66e",
};

function numberInput(id, fallback = 0) {
  const value = Number(els[id].value);
  return Number.isFinite(value) ? value : fallback;
}

function formatKwh(value) {
  if (Math.abs(value) >= 1_000_000) return `${(value / 1_000_000).toFixed(2)} GWh`;
  if (Math.abs(value) >= 1_000) return `${(value / 1_000).toFixed(2)} MWh`;
  return `${value.toFixed(1)} kWh`;
}

function formatTon(value) {
  if (!Number.isFinite(value)) return "Chưa xác định";
  return `${value.toFixed(2)} tCO2e`;
}

function formatPercent(value) {
  if (!Number.isFinite(value)) return "Chưa xác định";
  return `${value.toFixed(2)}%`;
}

function getParameter(key, field = "value") {
  return state.source.calculation_parameters[key]?.[field];
}

function buildDefaults(source) {
  const vehicles = source.assets.vehicles;
  const generation = source.assets.generation;
  const storage = source.assets.storage;
  const charging = source.assets.charging[0];
  const params = source.calculation_parameters;

  return {
    camcCount: vehicles.find((item) => item.model === "CAMC G2E").quantity,
    camcKm: 60000,
    camcKwhKm: params.EC_Electric_CAMC.value,
    camcDiesel: params.FE_Baseline_CAMC.value,
    farizonCount: vehicles.find((item) => item.model === "Farizon H9E").quantity,
    farizonKm: 60000,
    farizonKwhKm: params.EC_Electric_Farizon.value,
    farizonDiesel: params.FE_Baseline_Farizon.value,
    solarMw: generation.find((item) => item.model === "Solar áp mái").capacity_mwp,
    windKw: generation.find((item) => item.model === "Tua-bin gió trục đứng").total_power_kw,
    rmfcKw: generation.find((item) => item.model === "RMFC chạy Bio-Methanol").power_mw * 1000,
    rmfcDispatch: 100,
    rmfcEff: 40,
    vfbPowerMw: storage.find((item) => item.model.includes("VFB")).power_mw,
    vfbCapacityMwh: storage.find((item) => item.model.includes("VFB")).energy_capacity_mwh,
    vfbEff: params.Eff_VFB.value_percent,
    bessPowerMw: storage.find((item) => item.model.includes("BESS")).power_mw,
    bessCapacityMwh: storage.find((item) => item.model.includes("BESS")).energy_capacity_mwh,
    bessEff: params.Eff_BESS.value_percent,
    chargeEff: params.Eff_Charge.value_percent,
    transmissionLoss: params.Loss_Transmission.value_percent,
    chargerPowerMw: charging.total_design_power_mw,
  };
}

function applyDefaults() {
  for (const [id, value] of Object.entries(state.defaults)) {
    if (els[id]) els[id].value = value;
  }
  runSimulation({ persist: false });
}

function readSavedScenario() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    const saved = JSON.parse(raw);
    if (!saved || typeof saved !== "object") return null;
    return saved;
  } catch (error) {
    console.warn("Không đọc được cấu hình đã lưu", error);
    return null;
  }
}

function applySavedScenario(saved) {
  let applied = false;
  for (const id of inputIds) {
    if (Object.prototype.hasOwnProperty.call(saved, id) && els[id]) {
      els[id].value = saved[id];
      applied = true;
    }
  }
  if (saved.periodSelect) {
    periodSelect.value = saved.periodSelect;
    applied = true;
  }
  if (saved.monthSelect) {
    monthSelect.value = saved.monthSelect;
    applied = true;
  }
  return applied;
}

function saveScenario() {
  const payload = {};
  for (const id of inputIds) {
    payload[id] = els[id].value;
  }
  payload.periodSelect = periodSelect.value;
  payload.monthSelect = monthSelect.value;
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
  } catch (error) {
    console.warn("Không lưu được cấu hình mô phỏng", error);
  }
}

function resetToDefaults() {
  localStorage.removeItem(STORAGE_KEY);
  applyDefaults();
}

function readScenario() {
  return {
    camcCount: numberInput("camcCount"),
    camcKm: numberInput("camcKm"),
    camcKwhKm: numberInput("camcKwhKm"),
    camcDiesel: numberInput("camcDiesel"),
    farizonCount: numberInput("farizonCount"),
    farizonKm: numberInput("farizonKm"),
    farizonKwhKm: numberInput("farizonKwhKm"),
    farizonDiesel: numberInput("farizonDiesel"),
    solarKw: numberInput("solarMw") * 1000,
    windKw: numberInput("windKw"),
    rmfcKw: numberInput("rmfcKw"),
    rmfcDispatchFraction: numberInput("rmfcDispatch") / 100,
    rmfcEffFraction: numberInput("rmfcEff") > 0 ? numberInput("rmfcEff") / 100 : null,
    vfbPowerKw: numberInput("vfbPowerMw") * 1000,
    vfbCapacityKwh: numberInput("vfbCapacityMwh") * 1000,
    vfbEff: numberInput("vfbEff") / 100,
    bessPowerKw: numberInput("bessPowerMw") * 1000,
    bessCapacityKwh: numberInput("bessCapacityMwh") * 1000,
    bessEff: numberInput("bessEff") / 100,
    chargeEff: numberInput("chargeEff") / 100,
    transmissionLoss: numberInput("transmissionLoss") / 100,
  };
}

function calcFleet(scenario) {
  const camcAnnualKwh = scenario.camcCount * scenario.camcKm * scenario.camcKwhKm;
  const farizonAnnualKwh = scenario.farizonCount * scenario.farizonKm * scenario.farizonKwhKm;
  const camcDieselLiters = scenario.camcCount * scenario.camcKm * scenario.camcDiesel;
  const farizonDieselLiters = scenario.farizonCount * scenario.farizonKm * scenario.farizonDiesel;

  return {
    annualVehicleKwh: camcAnnualKwh + farizonAnnualKwh,
    annualDieselLiters: camcDieselLiters + farizonDieselLiters,
  };
}

function calcBaselineEmissions(dieselLiters) {
  const density = getParameter("Density_Diesel");
  const ncv = getParameter("NCV_Diesel");
  const efTtw = getParameter("EF_Diesel_combustion");
  const efWtt = getParameter("EF_Diesel_WTT");
  const ttw = (dieselLiters * density * ncv * efTtw) / 1e9;
  const wtt = (dieselLiters * density * ncv * efWtt) / 1e9;
  return { ttw, wtt, total: ttw + wtt };
}

function createStorage(powerKw, capacityKwh, efficiency) {
  return {
    powerKw: Math.max(0, powerKw),
    capacityKwh: Math.max(0, capacityKwh),
    efficiency: Math.min(1, Math.max(0.01, efficiency || 0.01)),
    soc: 0,
    charged: 0,
    discharged: 0,
    losses: 0,
  };
}

function chargeStorage(storage, availableKwh) {
  if (availableKwh <= 0 || storage.powerKw <= 0 || storage.capacityKwh <= 0) return 0;
  const storableInput = Math.min(availableKwh, storage.powerKw, (storage.capacityKwh - storage.soc) / storage.efficiency);
  const stored = storableInput * storage.efficiency;
  storage.soc += stored;
  storage.charged += storableInput;
  storage.losses += storableInput - stored;
  return storableInput;
}

function dischargeStorage(storage, neededKwh) {
  if (neededKwh <= 0 || storage.powerKw <= 0 || storage.capacityKwh <= 0) return 0;
  const output = Math.min(neededKwh, storage.powerKw, storage.soc);
  storage.soc -= output;
  storage.discharged += output;
  return output;
}

function aggregateDaily(hourly) {
  const days = [];
  for (let i = 0; i < hourly.length; i += 24) {
    const slice = hourly.slice(i, i + 24);
    const first = slice[0];
    const label = first.localTime.slice(5, 10);
    days.push({
      label,
      month: label.slice(0, 2),
      solarGenerated: sum(slice, "solarGenerated"),
      windGenerated: sum(slice, "windGenerated"),
      solar: sum(slice, "solarUsed"),
      wind: sum(slice, "windUsed"),
      rmfc: sum(slice, "rmfcUsed"),
      storage: sum(slice, "storageDischarge"),
      storageCharge: sum(slice, "storageCharge"),
      grid: sum(slice, "grid"),
      surplus: sum(slice, "surplus"),
      load: sum(slice, "load"),
    });
  }
  return days;
}

function sum(items, key) {
  return items.reduce((total, item) => total + item[key], 0);
}

function aggregateRows(rows, size, labelPrefix) {
  const groups = [];
  for (let i = 0; i < rows.length; i += size) {
    const slice = rows.slice(i, i + size);
    const index = groups.length + 1;
    groups.push({
      label: `${labelPrefix} ${String(index).padStart(2, "0")}`,
      month: slice[0].month,
      solarGenerated: sum(slice, "solarGenerated"),
      windGenerated: sum(slice, "windGenerated"),
      solar: sum(slice, "solar"),
      wind: sum(slice, "wind"),
      rmfc: sum(slice, "rmfc"),
      storage: sum(slice, "storage"),
      storageCharge: sum(slice, "storageCharge"),
      grid: sum(slice, "grid"),
      surplus: sum(slice, "surplus"),
      load: sum(slice, "load"),
    });
  }
  return groups;
}

function aggregateMonthly(rows) {
  const months = [];
  for (let month = 1; month <= 12; month += 1) {
    const monthKey = String(month).padStart(2, "0");
    const slice = rows.filter((item) => item.month === monthKey);
    months.push({
      label: `Tháng ${monthKey}`,
      month: monthKey,
      solarGenerated: sum(slice, "solarGenerated"),
      windGenerated: sum(slice, "windGenerated"),
      solar: sum(slice, "solar"),
      wind: sum(slice, "wind"),
      rmfc: sum(slice, "rmfc"),
      storage: sum(slice, "storage"),
      storageCharge: sum(slice, "storageCharge"),
      grid: sum(slice, "grid"),
      surplus: sum(slice, "surplus"),
      load: sum(slice, "load"),
    });
  }
  return months;
}

function balanceRows(dailyRows) {
  const period = periodSelect.value;
  monthSelect.disabled = period !== "day";
  if (period === "month") return aggregateMonthly(dailyRows);
  if (period === "week") return aggregateRows(dailyRows, 7, "Tuần");
  return monthSelect.value === "all" ? dailyRows : dailyRows.filter((item) => item.month === monthSelect.value);
}

function runDispatch(scenario, fleet) {
  const records = Math.min(state.pv.records.length, state.wind.records.length);
  const chargeEfficiency = Math.max(0.01, scenario.chargeEff);
  const transmissionFactor = 1 + Math.max(0, scenario.transmissionLoss);
  const hourlyVehicleLoad = fleet.annualVehicleKwh / records;
  const hourlySystemLoad = (hourlyVehicleLoad / chargeEfficiency) * transmissionFactor;
  const vfb = createStorage(scenario.vfbPowerKw, scenario.vfbCapacityKwh, scenario.vfbEff);
  const bess = createStorage(scenario.bessPowerKw, scenario.bessCapacityKwh, scenario.bessEff);
  const hourly = [];
  const totals = {
    solarGenerated: 0,
    windGenerated: 0,
    solarUsed: 0,
    windUsed: 0,
    rmfcUsed: 0,
    grid: 0,
    cleanSurplus: 0,
    load: 0,
    storageCharge: 0,
    transmissionLossKwh: hourlySystemLoad * records - fleet.annualVehicleKwh / chargeEfficiency,
  };

  for (let i = 0; i < records; i += 1) {
    const solar = scenario.solarKw * state.pv.records[i].electricity_kw_per_kw;
    const wind = scenario.windKw * state.wind.records[i].electricity_kw_per_kw;
    const renewable = solar + wind;
    let remainingLoad = hourlySystemLoad;
    const directClean = Math.min(renewable, remainingLoad);
    remainingLoad -= directClean;
    let surplus = Math.max(0, renewable - directClean);

    const bessCharge = chargeStorage(bess, surplus);
    surplus -= bessCharge;
    const vfbCharge = chargeStorage(vfb, surplus);
    surplus -= vfbCharge;
    const storageCharge = bessCharge + vfbCharge;

    const bessDischarge = dischargeStorage(bess, remainingLoad);
    remainingLoad -= bessDischarge;
    const vfbDischarge = dischargeStorage(vfb, remainingLoad);
    remainingLoad -= vfbDischarge;

    const rmfcPotential = scenario.rmfcKw * scenario.rmfcDispatchFraction;
    const rmfcUsed = Math.min(rmfcPotential, remainingLoad);
    remainingLoad -= rmfcUsed;

    const grid = Math.max(0, remainingLoad);
    const solarUsed = renewable > 0 ? directClean * (solar / renewable) : 0;
    const windUsed = directClean - solarUsed;
    const storageDischarge = bessDischarge + vfbDischarge;

    totals.solarGenerated += solar;
    totals.windGenerated += wind;
    totals.solarUsed += solarUsed;
    totals.windUsed += windUsed;
    totals.rmfcUsed += rmfcUsed;
    totals.grid += grid;
    totals.cleanSurplus += surplus;
    totals.storageCharge += storageCharge;
    totals.load += hourlySystemLoad;

    hourly.push({
      localTime: state.pv.records[i].local_time,
      solarGenerated: solar,
      windGenerated: wind,
      solarUsed,
      windUsed,
      rmfcUsed,
      storageDischarge,
      storageCharge,
      grid,
      surplus,
      load: hourlySystemLoad,
    });
  }

  return {
    hourly,
    daily: aggregateDaily(hourly),
    totals,
    storage: {
      charged: bess.charged + vfb.charged,
      discharged: bess.discharged + vfb.discharged,
      losses: bess.losses + vfb.losses,
      finalSoc: bess.soc + vfb.soc,
    },
  };
}

function calcProjectEmissions(dispatch, scenario, fleet) {
  const efGrid = getParameter("EF_Grid_location");
  const efSolarWind = getParameter("EF_SolarWind_EP");
  const accountedEnergy = Math.max(0, fleet.annualVehicleKwh);
  const suppliedEnergy =
    dispatch.totals.grid +
    dispatch.totals.solarUsed +
    dispatch.totals.windUsed +
    dispatch.storage.discharged +
    dispatch.totals.rmfcUsed;
  const shareBase = suppliedEnergy > 0 ? suppliedEnergy : 1;
  const gridChargeKwh = accountedEnergy * (dispatch.totals.grid / shareBase);
  const solarWindChargeKwh =
    accountedEnergy * ((dispatch.totals.solarUsed + dispatch.totals.windUsed + dispatch.storage.discharged) / shareBase);
  const rmfcChargeKwh = accountedEnergy * (dispatch.totals.rmfcUsed / shareBase);
  const grid = (gridChargeKwh * efGrid) / 1000;
  const solarWind = (solarWindChargeKwh * efSolarWind) / 1000;
  let rmfc = null;
  if (scenario.rmfcEffFraction) {
    const efRmfc = 0.144 / scenario.rmfcEffFraction;
    rmfc = (rmfcChargeKwh * efRmfc) / 1000;
  }
  return {
    grid,
    solarWind,
    rmfc,
    verifiedTotal: grid + solarWind + (rmfc || 0),
    rmfcIsVerified: rmfc !== null,
  };
}

function runSimulation(options = {}) {
  if (!state.source || !state.pv || !state.wind) return;
  if (options.persist !== false) saveScenario();
  const scenario = readScenario();
  const fleet = calcFleet(scenario);
  const baseline = calcBaselineEmissions(fleet.annualDieselLiters);
  const dispatch = runDispatch(scenario, fleet);
  const project = calcProjectEmissions(dispatch, scenario, fleet);
  const reduction = baseline.total - project.verifiedTotal;
  const reductionRate = baseline.total > 0 ? (reduction / baseline.total) * 100 : 0;
  const renewableSupply = dispatch.totals.solarUsed + dispatch.totals.windUsed + dispatch.storage.discharged + dispatch.totals.rmfcUsed;
  const renewableShare = dispatch.totals.load > 0 ? (renewableSupply / dispatch.totals.load) * 100 : 0;

  renderKpis({ fleet, baseline, dispatch, project, reduction, reductionRate, renewableShare });
  renderCharts({ dispatch, baseline, project });
}

function renderKpis(model) {
  kpiEls.load.textContent = formatKwh(model.fleet.annualVehicleKwh);
  kpiEls.renewable.textContent = formatPercent(model.renewableShare);
  kpiEls.grid.textContent = formatKwh(model.dispatch.totals.grid);
  kpiEls.rmfc.textContent = formatKwh(model.dispatch.totals.rmfcUsed);
  kpiEls.surplus.textContent = formatKwh(model.dispatch.totals.cleanSurplus);
  kpiEls.baseline.textContent = formatTon(model.baseline.total);
  kpiEls.project.textContent = model.project.rmfcIsVerified
    ? formatTon(model.project.verifiedTotal)
    : `${formatTon(model.project.verifiedTotal)}*`;
  kpiEls.reduction.textContent = formatTon(model.reduction);
  kpiEls.reductionRate.textContent = formatPercent(model.reductionRate);
  kpiEls.pvCf.textContent = formatPercent(state.pv.metadata.capacity_factor_percent);
  kpiEls.windCf.textContent = formatPercent(state.wind.metadata.capacity_factor_percent);
  kpiEls.storageCharge.textContent = formatKwh(model.dispatch.storage.charged);
  kpiEls.storageDischarge.textContent = formatKwh(model.dispatch.storage.discharged);
  kpiEls.storageLoss.textContent = formatKwh(model.dispatch.storage.losses);
  kpiEls.transmissionLoss.textContent = formatKwh(model.dispatch.totals.transmissionLossKwh);
  kpiEls.rmfcStatus.textContent = model.project.rmfcIsVerified
    ? "Phát thải RMFC: đã đưa vào tổng"
    : "Phát thải RMFC: chưa xác định, chưa đưa vào tổng đã kiểm chứng";
}

function chartOptions(stacked = false) {
  return {
    responsive: true,
    maintainAspectRatio: false,
    interaction: { mode: "index", intersect: false },
    plugins: {
      legend: { position: "bottom" },
      tooltip: {
        callbacks: {
          label: (context) => `${context.dataset.label}: ${formatKwh(context.parsed.y)}`,
        },
      },
    },
    scales: {
      x: { stacked, ticks: { maxTicksLimit: 12 } },
      y: {
        stacked,
        beginAtZero: true,
        ticks: { callback: (value) => formatKwh(Number(value)) },
      },
    },
  };
}

function balanceChartOptions() {
  return {
    responsive: true,
    maintainAspectRatio: false,
    interaction: { mode: "index", intersect: false },
    plugins: {
      legend: { position: "bottom" },
      tooltip: {
        callbacks: {
          label: (context) => `${context.dataset.label}: ${formatKwh(context.parsed.y)}`,
        },
      },
    },
    scales: {
      x: { stacked: true, ticks: { maxTicksLimit: 12 } },
      y: {
        stacked: true,
        beginAtZero: true,
        ticks: { callback: (value) => formatKwh(Number(value)) },
      },
    },
  };
}

function upsertChart(key, context, config) {
  if (state.charts[key]) {
    state.charts[key].data = config.data;
    state.charts[key].options = config.options;
    state.charts[key].update();
    return;
  }
  state.charts[key] = new Chart(context, config);
}

function periodEmissionRows(rows, baseline, project, dispatch) {
  const totalLoad = dispatch.totals.load || 1;
  const totalSupplied =
    dispatch.totals.grid +
      dispatch.totals.solarUsed +
      dispatch.totals.windUsed +
      dispatch.storage.discharged +
      dispatch.totals.rmfcUsed || 1;
  let cumulativeBaseline = 0;
  let cumulativeProject = 0;
  return rows.map((row) => {
    const loadShare = row.load / totalLoad;
    const supplied = row.grid + row.solar + row.wind + row.storage + row.rmfc;
    const supplyShare = supplied / totalSupplied;
    cumulativeBaseline += baseline.total * loadShare;
    cumulativeProject += project.verifiedTotal * supplyShare;
    return {
      label: row.label,
      baseline: cumulativeBaseline,
      project: cumulativeProject,
    };
  });
}

function emissionsAreaOptions() {
  return {
    responsive: true,
    maintainAspectRatio: false,
    interaction: { mode: "index", intersect: false },
    plugins: {
      legend: { position: "bottom" },
      tooltip: {
        callbacks: {
          label: (context) => `${context.dataset.label}: ${context.parsed.y.toFixed(3)} tCO2e`,
        },
      },
    },
    scales: {
      x: { ticks: { maxTicksLimit: 12 } },
      y: {
        beginAtZero: true,
        ticks: { callback: (value) => `${Number(value).toFixed(2)} tCO2e` },
      },
    },
  };
}

function renderCharts({ dispatch, baseline, project }) {
  const daily = balanceRows(dispatch.daily);
  upsertChart("balance", document.getElementById("balanceChart"), {
    type: "bar",
    data: {
      labels: daily.map((item) => item.label),
      datasets: [
        barDataset("Solar", daily, "solarGenerated", colors.solar, "supply"),
        barDataset("Gió", daily, "windGenerated", colors.wind, "supply"),
        barDataset("RMFC", daily, "rmfc", colors.rmfc, "supply"),
        barDataset("Xả pin", daily, "storage", colors.storage, "supply"),
        barDataset("Lưới", daily, "grid", colors.grid, "supply"),
        allocationDataset("Sạc xe", daily, "load", "#141a16"),
        allocationDataset("Nạp pin", daily, "storageCharge", "#6d8cc7"),
        allocationDataset("Dư sạch", daily, "surplus", colors.surplus),
      ],
    },
    options: balanceChartOptions(),
  });

  const periodEmissionsPanel = document.getElementById("periodEmissionsPanel");
  if (periodEmissionsPanel && !periodEmissionsPanel.hidden) {
    const periodEmissions = periodEmissionRows(daily, baseline, project, dispatch);
    upsertChart("periodEmissions", document.getElementById("periodEmissionsChart"), {
      type: "line",
      data: {
        labels: periodEmissions.map((item) => item.label),
        datasets: [
          areaDataset("Đường cơ sở lũy kế", periodEmissions, "baseline", colors.baseline),
          areaDataset("Dự án lũy kế", periodEmissions, "project", colors.project),
        ],
      },
      options: emissionsAreaOptions(),
    });
  }

  upsertChart("energyMix", document.getElementById("energyMixChart"), {
    type: "bar",
    data: {
      labels: ["Mặt trời trực tiếp", "Gió trực tiếp", "RMFC", "Xả lưu trữ", "Điện lưới", "Năng lượng sạch dư"],
      datasets: [
        {
          label: "kWh/năm",
          data: [
            dispatch.totals.solarUsed,
            dispatch.totals.windUsed,
            dispatch.totals.rmfcUsed,
            dispatch.storage.discharged,
            dispatch.totals.grid,
            dispatch.totals.cleanSurplus,
          ],
          backgroundColor: [colors.solar, colors.wind, colors.rmfc, colors.storage, colors.grid, colors.surplus],
          borderWidth: 0,
        },
      ],
    },
    options: chartOptions(false),
  });

  upsertChart("emissions", document.getElementById("emissionsChart"), {
    type: "bar",
    data: {
      labels: ["Đường cơ sở TTW", "Đường cơ sở WTT", "Dự án: điện lưới", "Dự án: mặt trời/gió", "Dự án: RMFC"],
      datasets: [
        {
          label: "tCO2e/năm",
          data: [baseline.ttw, baseline.wtt, project.grid, project.solarWind, project.rmfc || 0],
          backgroundColor: [colors.baseline, "#d9837a", colors.grid, colors.project, colors.rmfc],
          borderWidth: 0,
        },
      ],
    },
    options: {
      ...chartOptions(false),
      plugins: {
        ...chartOptions(false).plugins,
        tooltip: {
          callbacks: {
            label: (context) => `${context.dataset.label}: ${context.parsed.y.toFixed(2)}`,
          },
        },
      },
      scales: {
        x: { ticks: { maxRotation: 0, autoSkip: false } },
        y: { beginAtZero: true },
      },
    },
  });
}

function dataset(label, rows, key, color) {
  return {
    label,
    data: rows.map((item) => item[key]),
    borderColor: color,
    backgroundColor: `${color}55`,
    fill: true,
    pointRadius: 0,
    tension: 0.25,
  };
}

function areaDataset(label, rows, key, color) {
  return {
    label,
    data: rows.map((item) => item[key]),
    borderColor: color,
    backgroundColor: `${color}38`,
    fill: true,
    pointRadius: 0,
    tension: 0.25,
  };
}

function barDataset(label, rows, key, color, stack) {
  return {
    type: "bar",
    label,
    data: rows.map((item) => item[key]),
    backgroundColor: color,
    borderWidth: 0,
    stack,
    order: 2,
  };
}

function allocationDataset(label, rows, key, color) {
  return {
    type: "bar",
    label,
    data: rows.map((item) => item[key]),
    backgroundColor: `${color}66`,
    borderColor: color,
    borderWidth: 1,
    borderDash: [3, 3],
    stack: "allocation",
    order: 2,
  };
}

async function loadJson(path) {
  const candidates = Array.isArray(path) ? path : [path];
  const errors = [];
  for (const candidate of candidates) {
    try {
      const response = await fetch(candidate);
      if (!response.ok) {
        errors.push(`${candidate}: ${response.status}`);
        continue;
      }
      return response.json();
    } catch (error) {
      errors.push(`${candidate}: ${error.message}`);
    }
  }
  throw new Error(`Không tải được dữ liệu. Đã thử: ${errors.join("; ")}`);
}

async function init() {
  try {
    const [source, pv, wind] = await Promise.all([loadJson(DATA_PATHS.params), loadJson(DATA_PATHS.pv), loadJson(DATA_PATHS.wind)]);
    state.source = source;
    state.pv = pv;
    state.wind = wind;
    state.defaults = buildDefaults(source);
    applyDefaults();
    const saved = readSavedScenario();
    if (saved && applySavedScenario(saved)) {
      runSimulation();
    }
    kpiEls.dataStatus.textContent = `Đã tải ${pv.records.length} giờ PV + ${wind.records.length} giờ gió`;
  } catch (error) {
    kpiEls.dataStatus.textContent = "Không tải được dữ liệu";
    console.error(error);
  }
}

for (const id of inputIds) {
  els[id].addEventListener("input", runSimulation);
}

document.getElementById("resetButton").addEventListener("click", resetToDefaults);
monthSelect.addEventListener("change", runSimulation);
periodSelect.addEventListener("change", runSimulation);

init();
