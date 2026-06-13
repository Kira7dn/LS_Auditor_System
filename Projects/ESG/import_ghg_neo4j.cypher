// ==========================================
// NEO4J GRAPH INITIALIZATION FOR GHG PROTOCOL
// ==========================================

// 1. Clear database (optional, run with caution)
// MATCH (n) DETACH DELETE n;

// 2. Create Constraints for Unique IDs
CREATE CONSTRAINT unique_standard_id IF NOT EXISTS FOR (s:Standard) REQUIRE s.id IS UNIQUE;
CREATE CONSTRAINT unique_principle_id IF NOT EXISTS FOR (p:Principle) REQUIRE p.id IS UNIQUE;
CREATE CONSTRAINT unique_boundary_id IF NOT EXISTS FOR (b:Boundary) REQUIRE b.id IS UNIQUE;
CREATE CONSTRAINT unique_scope_id IF NOT EXISTS FOR (sc:Scope) REQUIRE sc.id IS UNIQUE;
CREATE CONSTRAINT unique_source_id IF NOT EXISTS FOR (es:EmissionSource) REQUIRE es.id IS UNIQUE;
CREATE CONSTRAINT unique_method_id IF NOT EXISTS FOR (m:CalculationMethod) REQUIRE m.id IS UNIQUE;

// 3. Create Core Standard Node
MERGE (std:Standard {id: "ghg-protocol-corporate", name: "GHG Protocol Corporate Standard", version: "Revised Edition", publisher: "WRI/WBCSD"});

// 4. Create Core Principles (Chapter 1)
MERGE (p1:Principle {id: "relevance", name: "Relevance", description: "Ensure the GHG inventory appropriately reflects the GHG emissions of the company and serves decision-making needs."})
MERGE (p2:Principle {id: "completeness", name: "Completeness", description: "Account for and report on all GHG emission sources and activities within the chosen inventory boundary. Disclose and justify exclusions."})
MERGE (p3:Principle {id: "consistency", name: "Consistency", description: "Use consistent methodologies to allow for meaningful comparisons of emissions over time."})
MERGE (p4:Principle {id: "transparency", name: "Transparency", description: "Address all relevant issues in a factual and coherent manner, based on a clear audit trail."})
MERGE (p5:Principle {id: "accuracy", name: "Accuracy", description: "Ensure that the quantification of GHG emissions is systematically neither over nor under actual emissions, and uncertainties are reduced."})

MERGE (std)-[:UNDERPINNED_BY]->(p1)
MERGE (std)-[:UNDERPINNED_BY]->(p2)
MERGE (std)-[:UNDERPINNED_BY]->(p3)
MERGE (std)-[:UNDERPINNED_BY]->(p4)
MERGE (std)-[:UNDERPINNED_BY]->(p5);

// 5. Create Boundary Approaches (Chapter 3)
MERGE (b1:Boundary {id: "equity_share", name: "Equity Share Approach", type: "Organizational", description: "A company accounts for GHG emissions from operations according to its share of equity in the operation."})
MERGE (b2:Boundary {id: "control_financial", name: "Financial Control", type: "Organizational", description: "A company has financial control over the operation if the company has the ability to direct the financial and operating policies."})
MERGE (b3:Boundary {id: "control_operational", name: "Operational Control", type: "Organizational", description: "A company has operational control over an operation if the company or one of its subsidiaries has the full authority to introduce and implement its operating policies."})

MERGE (std)-[:DEFINES_BOUNDARY]->(b1)
MERGE (std)-[:DEFINES_BOUNDARY]->(b2)
MERGE (std)-[:DEFINES_BOUNDARY]->(b3);

// 6. Create Operational Boundaries (Scopes) (Chapter 4)
MERGE (sc1:Scope {id: "scope_1", level: 1, name: "Scope 1 (Direct GHG Emissions)", description: "Direct emissions from sources owned or controlled by the reporting company."})
MERGE (sc2:Scope {id: "scope_2", level: 2, name: "Scope 2 (Electricity Indirect GHG Emissions)", description: "Indirect emissions from the generation of purchased electricity consumed by the company."})
MERGE (sc3:Scope {id: "scope_3", level: 3, name: "Scope 3 (Other Indirect GHG Emissions)", description: "Optional reporting category that allows for the treatment of all other indirect emissions."})

MERGE (std)-[:GOVERNS]->(sc1)
MERGE (std)-[:GOVERNS]->(sc2)
MERGE (std)-[:GOVERNS]->(sc3);

// 7. Create Sample Emission Sources and Methodologies (Chapter 4 & Chapter 6)
MERGE (es1:EmissionSource {id: "stationary_combustion", name: "Stationary Combustion", category: "Direct"})
MERGE (es2:EmissionSource {id: "mobile_combustion", name: "Mobile Combustion", category: "Direct"})
MERGE (es3:EmissionSource {id: "purchased_electricity", name: "Purchased Electricity Consumption", category: "Indirect"})
MERGE (es4:EmissionSource {id: "waste_generation", name: "Waste Generation in Operations", category: "Value Chain Indirect"})

MERGE (sc1)-[:INCLUDES_SOURCE]->(es1)
MERGE (sc1)-[:INCLUDES_SOURCE]->(es2)
MERGE (sc2)-[:INCLUDES_SOURCE]->(es3)
MERGE (sc3)-[:INCLUDES_SOURCE]->(es4);

// Methodologies
MERGE (m1:CalculationMethod {id: "fuel_analysis", name: "Fuel Analysis Method", formula: "Emissions = Fuel Consumed * Carbon Content Factor * Oxidation Fraction * (44/12)"})
MERGE (m2:CalculationMethod {id: "market_based_electricity", name: "Market-Based Method", formula: "Emissions = MWh * Supplier-specific Emission Factor"})
MERGE (m3:CalculationMethod {id: "location_based_electricity", name: "Location-Based Method", formula: "Emissions = MWh * Grid Average Emission Factor"})

MERGE (es1)-[:CALCULATED_USING]->(m1)
MERGE (es3)-[:CALCULATED_USING]->(m2)
MERGE (es3)-[:CALCULATED_USING]->(m3);
