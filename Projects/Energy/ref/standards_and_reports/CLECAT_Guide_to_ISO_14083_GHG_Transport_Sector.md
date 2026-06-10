# CLECAT_Guide_to_ISO_14083_GHG_Transport_Sector

- Converted from: `CLECAT_Guide_to_ISO_14083_GHG_Transport_Sector.pdf`
- Total Pages: 66

---

## Page 1

  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
                                                                                                                                           
 
 
 
 
Greenhouse gas emissions in 
the transport sector  
Guide to I SO 14083 
Application and examples 


---

## Page 2

Imprint 
 
Editor of the English translation and support:       
CLECAT  
Rue du Commerce 77   
1040 Brussels   
Phone: +32 2 503 47 05   
info@clecat.org  
Internet: www.clecat.org  
 
 
 
This Guide is based on a publication by the German Federal Environment Agency : 
 
Umweltbundesamt: “Treibhausgasemissionen im Transportsektor – Leitfaden zur 
ISO 14083” 
https://www.umweltbundesamt.de/publikationen/treibhausgasemissionen -im-
transportsektor 
 
 
 
 
Authors: 
Dr.-Ing. Kirsten Biemann, Wolfram Knörr  
ifeu Institute, Heidelberg, Germany 
Dr.-Ing. Kerstin Dobers, Jan-Philipp Jarmer 
Fraunhofer IML, Dortmund, Germany 
 
The authors are responsible for the content of this 
publication. 
 
 
 
 
 
 
 
 
Acknowledgement 
In the preparation of this guide, a number of people contributed with their 
long-term expertise on GHG emissions assessment in the transport sector 
and provided valuable feedback in the context of a review. 
The authors would like to take this opportunity to express their sincere thanks to, among others: 
Noelle Froehlich (DHL Group), Patric Pütz (DHL Group), Andrea Schön (Smart Freight Centre) 
and Adrian Wojnowski (Smart Freight Centre). 
 


---

## Page 3

Foreword 
 
As the global economy increasingly recognises the urgent need to decarbonise supply chains, the 
logistics industry faces rising expectations for reducing greenhouse gas (GHG) emissions. Transporting 
goods and passengers efficiently and sustainably has become crucial, as regulatory requirements, 
voluntary climate targets, and consumer demand for sustainable products intensify. 
The quantification of GHG emissions in the transport sector is a significant challenge, one that will 
continue to gain importance with the EU Corporate Sustainability Reporting Directive (CSRD), which 
came into force on the 5th of January 2023. This Directive requires companies above a certain size to 
regularly report on their sustainability efforts, including emissions from their supply chains. As 
companies adapt to these new obligations, sound assessments and collaboration with supply chain 
partners will be essential. 
The ISO 14083 ‘Greenhouse gases - Quantification and reporting of greenhouse gas emissions arising 
from transport chain operations’, published in March 2023, provides a corresponding basis for the 
international standardisation of the calculation and reporting of emissions from (global) transport 
chains. This standard offers a comprehensive methodology for transport and logistics companies to 
calculate and assess GHG emissions from global and regional supply chains across different modes of 
transport. This facilitates consistent and comparable sustainability reporting.  
Based on a competitive call, UBA commissioned ifeu and Fraunhofer IML to develop a practical guide to 
support businesses in implementing ISO 14083. This guide includes case studies relating to both freight 
and passenger transport, demonstrating the application of the standard and addressing challenges that 
may arise in the course of its application.  
I am confident that this guide provides a valuable resource for assessing the climate impact of 
transportation activities and assisting companies in reporting their GHG emissions transparently.  
 
Dirk Messner  
President of the German Environment Agency (UBA) 
 
 
 
 


---

## Page 4

 
 
Table of contents 
Foreword .................................................................................... 3 
Glossary of key terms ................................................................ 5 
List of figures and tables .......................................................... 7 
Introduction ................................................................................ 9 
1.1 Overview .............................................................................................. 10 
1.2 Terms and basics ................................................................................ 11 
1.3 Guide to the guide – Where can you find what? ................................... 13 
Basic procedure ......................................................................... 15 
2.1 Basics of assessment and system boundaries  ...................................... 15 
2.2 Data quality and data categories  ......................................................... 18 
2.3 Introduction to step -by-step GHG emissions calculation  .................... 19 
Transport chain elements and activity data ............................ 21 
3.1 Breakdown of the transport chain into transport chain elements  ........ 21 
3.2 Calculation of the transport and hub activity of the transport chain 
elements .............................................................................................. 21 
3.3 Case examples Part 1 .......................................................................... 23 
Getting started with calculation and data collection ............... 27 
4.1 Establishment of transport and hub operation categories  ................... 27 
4.2 Calculating the GHG emission intensities ............................................ 29 
4.3 Case examples Part 2 .......................................................................... 42 
Calculation of GHG emissions of a transport chain ................. 47 
5.1 From GHG emission intensity to GHG emissions of TCEs and TC ......... 47 
5.2 Case examples Part 3 .......................................................................... 47 
Reporting according to ISO 14083 ........................................... 50 
6.1 Short reports ....................................................................................... 50 
6.2 Additional information as part of the reporting  ................................... 52 
6.3 Case examples Part 4 .......................................................................... 55 
References ...................................................................................... 59 
Appendix ........................................................................................ 60 
A.1 Relevant conversion factors  ................................................................. 60 
A.2 TOC characteristics of the different modes of transport  ...................... 60 
A.3 GHG emission factors of common energy carriers  ............................. 61 
A.4 GHG emission factors of common refrigerants  .................................. 63 
A.5 GHG emission intensities (transport/hubs) and their sources  .............. 65 

---

## Page 5

 
 
Glossary of key terms 
 
 
 
Term: English  Explanation / Reference  
Total GHG emissions 
summarises GHG emissions from energy provision and operation, see 
section 1.2; replaces term in EN 16258: Well-to-Wheel (WTW) 
Formula symbol 𝐺𝑇 
Greenhouse Gas (GHG) 
Protocol Scope 1/2/3 
supports the calculation of greenhouse gases and includes three perspectives, so-
called "Scopes" that take different emissions into account, see section 1.1 
Hub activity 
quantifies the throughput of a hub, is usually expressed in tonnes (t) or number of 
passengers (pax), see section 3.2 
Formula symbol H 
Hub operation (HO) describes the transfer of cargo (e.g. in a logistics site) or of people (e.g. in 
a passenger terminal), see section 3.2 
Hub operation category 
(HOC) summarises hub operations (HO) with similar characteristics, see section 3.2 
Shortest feasible 
distance (SFD) 
describes the shortest suitable route, taking into account the infrastructure options 
for a given vehicle type, see section 3.2.1 
Great circle distance 
(GCD) 
describes the shortest distance between two points of the earth's surface along the 
globe, see section 3.2.1 
Primary data 
result from a direct measurement or can be calculated based on direct measured 
values, see sections 2.2 and 4.2.3; replaces term in EN 16258: individual measured 
values / specific values of a transport service provider / fleet values of a transport 
service provider 
Secondary data do not meet the requirements for primary data and include modelled data and default 
values, see sections 2.2 and 4.2.3 
GHG activity includes activities that cause GHG emissions, such as energy consumption, 
methane slip, refrigerant losses, see section 1.2 
Operation GHG 
emissions 
refers to the release of greenhouse gases due to the operation of vehicles or hubs, see 
section 1.2; replaces term in EN 16258: Tank-to-Wheel (TTW) 
Formula symbol 𝐺𝑉𝑂 or 𝐺𝐻𝐸𝑂 
Energy provision GHG 
emissions 
refers to the release of greenhouse gases during the production, storage, processing 
and distribution of energy carriers (including electricity) for use in transport chains, 
see section 1.2; replaces term in EN 16258: Well-to-Tank (WTT)  
Formula symbol 𝐺𝑉𝐸𝑃 or 𝐺𝐻𝐸𝐸𝑃 
GHG emission factor allows the conversion of GHG activity (i.e. energy consumption (fuel, electricity) and 
refrigerant leakage) into GHG emissions, see section 4.2.1 Formula symbol ε 
GHG emission intensity 
describes the GHG emissions related to corresponding transport or hub activities, see 
section 4.2 
Formula symbol g 

---

## Page 6

 
 
Transport activity 
quantifies the freight or passenger transport of e.g. a transport chain or a transport 
chain element, is usually measured in tonne-kilometres (tkm) or passenger-
kilometres (pkm), see section 3.2 
Formula symbol T 
Transport chain (TC) describes the transport of cargo or passengers from a point of origin to a destination 
and is specified by the sequence of transport chain elements (TCEs), see section 3.1 
Transport chain 
element (TCE) 
describes a section of a transport chain within which freight or persons are 
transported by a vehicle on a leg of the transport chain or pass through a hub, see 
section 3.1; replaces term in EN 16258: Leg 
Transport operation 
(TO) 
represents the use of a vehicle for the carriage of cargo and/or passengers, see 
section 3.2 
Transport operation 
category (TOC) 
summarises transport operations (TO) with similar characteristics over a certain 
period of time, see section 3.2; replaces term in EN 16258: Vehicle operation system 

---

## Page 7

Figures 
 
Figure 1 
Context of the standards  ............................................................................................................. 10 
Figure 2 
Example of a transport chain of freight with possible transport and hub operation categories  ........................... 12 
Figure 3 
Steps to calculate GHG emissions for a transport chain  ....................................................................... 19 
Figure 4 
Which steps are described in which chapters?  .................................................................................... 20 
Figure 5 
Illustration of steps 1 and 2: Transport chain elements  ......................................................................... 24 
Figure 6 
Collection and delivery round ........................................................................................................ 33 
Figure 7 
Illustration of steps 3 and 4: Assignment of TOC and TO to the transport chain to be evaluated  .........................43 
Figure 8 
Illustration of steps 5 and 6: GHG emissions and GHG emission intensities of the   
transport chain elements and transport chain  ................................................................................... 49 

---

## Page 8

Tables 
 
Table 1 
Hub operations to be included (yes), excluded (no) and optional in the GHG emissions calculation  ..................... 17 
Table 2 
GHG emissions from operations at hubs premises that should be assigned to inbound or outbound transport ........ 18 
Table 3 
Distances and distance adjustment factors ....................................................................................... 23 
Table 4 
HOC-characteristics ................................................................................................................... 29 
Table 5 
Passenger equivalent  values of Ro-Pax ferries and trains  ...................................................................... 32 
Table 6 
Allocation of a collection and delivery round ..................................................................................... 34 
Table 7 
Primary data on freight transhipment  in Hub 1 and Hub 2 ...................................................................... 36 
Table 8 
Origin of consumption data  .......................................................................................................... 38 
Table 9 
Data for Case example B ............................................................................................................. 45 
Table 10 
Elements of the short report at the level of transport or hub services  ........................................................ 51 
Table 11 
Elements of the short report at the o rganisational level ........................................................................ 51 
Table 12 
Reporting when using secondary data  ............................................................................................. 52 
Table 13 
Documentation of the emission factors of fuels and electricity  ................................................................ 54 
Table 14 
Short report on the Case example  A ................................................................................................ 55 
Table 15 
Reporting for the use of secondary data in Case example A for TCE 1, 3 and 5  ............................................. 56 
Table 16 
Short report on the Case example B ................................................................................................ 58 
Table 17 
GHG emission factors of European energy carriers .............................................................................. 62 
Table 18 
Focus on heating at hubs: GHG emission factors of European energy carriers .............................................. 63 
Table 19 
Exemplary emission factors for refrigerants (in g CO 2e per g refrigerant type)  .............................................. 64 

---

## Page 9

 
 
 
 
 
1 Introduction 
 
Greenhouse gas (GHG) emissions such as carbon 
dioxide or methane are caused in transport chains for 
passengers and freight by transport activities, 
processes at individual sites or services. The 
quantification of these emissions with their 
corresponding classification is fundamental in the 
current sustainability discourse.  
The European standard EN 16258 was published 
already in 2012 and focussed this topic. However, 
since there was still room for interpretation in the 
application of this standard and the standard was 
only applied at the European level, working groups 
were formed over time, aimed in particular at 
international standardisation. In this context, the 
Global Logistics Emissions Council (GLEC), which is 
managed by the Smart Freight Centre (SFC) and offers 
an industry guide for quantifying GHG emissions in 
the form of the GLEC Framework (Smart Freight 
Centre 2023), deserves special mention. The 
consideration of hub processes is being investigated 
by the Fraunhofer Institute for Material Flow and 
Logistics IML, among others, and described in more 
detail in the "Guide for Greenhouse Gas Emissions 
Accounting for Logistics Hubs" (Dobers and Jarmer 
2023). 
 
These and other activities have led to the 
development of an international standard 
since 2019, taking into account the latest 
findings. In March 2023, the ISO 14083 
standard "Greenhouse gases – Quantification 
and reporting of greenhouse gas emissions 
arising from transport chain
operations" was published, offering an international 
standardisation of the calculation and reporting of 
emissions from (global) transport chains. EN ISO 
14083 replaces EN 16258:2012 and, in addition to 
transport operations, also covers processes and the 
associated GHG emissions at sites (hubs) that enable 
the transfer of passengers or freight.  
 
The new ISO 14083 can be used for all applications in 
which GHG emissions from transports and hubs are 
quantified. It covers both passenger and freight 
transport by all means of transport and can be used 
for individual vehicles/transports as well as for 
vehicle fleets/groups of transport operations as well 
as for single or multiple hubs. Possible applications for 
the standard include company annual reports, GHG 
accounting tools for transports and hubs, 
disseminating information on GHG emissions from 
transport and transhipment/passenger transfer 
(either to specific groups of people or to the general 
public) and many other applications. This means that 
the standard is suitable for companies in the transport 
industry (e.g. public transport associations, shippers, 
freight forwarders) as well as for companies with 
another business area in which transports play a role 
in GHG reporting, and many other applications.  
1 Introduction 

---

## Page 10

10 
 
 
Overview   
 
This guideline is intended to assist in the uniform 
calculation and reporting of GHG emissions along 
transport chains. Requirements and calculation 
options resulting from ISO 14083 are presented and 
new terms and abbreviations are explained. 
Continuous examples illustrate the application of the 
standard and address challenges that may arise in 
the application of the standard. 
1.1 Overview 
1.1.1 How does ISO 14083 relate to other 
standards and regulations? 
ISO 14083 does not stand alone but is part of a 
number of other international standards for the 
quantification of environmental impacts and GHG 
emissions and specifies general principles for 
calculating GHG emissions in passenger and freight 
transport. Thus, the results of ISO 14083 can be used 
as a starting point for many further analyses, e.g. 
corporate carbon footprint (see ISO 14064), product 
carbon footprint (see ISO 14067or life cycle 
assessment
 
Figure 1 
Context of the standards   
 
 
 
 
Source: Detail from ISO 14083 Image 3 


---

## Page 11

11 
 
 
Overview  
 
 
 
(14040/44). Figure 1 shows links between ISO 
14083 and other international standards using the 
example of a freight transport chain. In addition, ISO 
14083 takes the requirements of the Greenhouse 
Gas Protocol (GHG Protocol) into account with its 
standards on corporate accounting and reporting 
(World Resource Institute and World Business 
Council for Sustainable Development 2011) and 
Scope 3 processes (Ranganathan et al. 2004). 
 
In addition, the publication of the new European 
standard EN 17837 "Parcel delivery Environmental 
Footprint: Methodology for calculation and 
declaration of GHG emissions and air pollutants of 
parcel logistics delivery services" has been 
published. This specifies some of the requirements 
of ISO 14083 with a focus on the parcel sector. In 
order to comply with the international 
standardisation work, it is therefore recommended 
that ISO 14083-compliant GHG emission 
calculations and reports to be implemented. This is 
because a proposal for a Regulation on the reporting 
of greenhouse gas emissions from transport services 
has already been submitted at the level of the 
European Commission (European Commission 
2023). This provides for the use of the EN ISO 14083 
standard as a reference method for the calculation 
of GHG emissions from transport services and is to 
be accompanied in the future by a central EU 
database for GHG emission factors, which are 
essential in GHG emission calculations. 
 
1.1.2 How is ISO 14083 structured? 
The wide variety of ways of transporting 
passengers and freight makes it necessary to 
establish calculation rules and uniform 
specifications on the system boundaries for GHG 
emission calculations. Therefore, ISO 14083 
defines which processes that release GHG 
emissions into the atmosphere must be included 
in the quantification. These emissions fall under 
the normative scope. In addition, the ISO describes 
optional processes that may be covered. These 
emissions fall under the informative scope. In 
addition, processes that shall not be included are 
explicitly excluded. 
The main body of ISO 14083 first provides general content 
and information on the calculation of GHG emissions 
(Sections 1 to 5) and then specific topics on data collection, 
allocation and reporting in the context of the passenger and 
freight transport (sections 6 to 13). 
The main part is supplemented by the annexes. Annexes A 
to J cover the normative scope and describe details of the 
modes of transport and hubs where they are part of a 
transport chain, as well as refrigerant leakages and GHG 
emission factors. 
 
The informative scope includes Annexes K to R, which – 
in addition to further guidance on selected topics such as 
the modelling of GHG emissions of transport chains – 
optionally classify topics to be taken into account, such 
as transport packaging, or refer to example default 
values for selected transport or logistics services. 
 
For information: the German version DIN EN ISO 14083 
also has an informative Annex S, which summarises the 
main technical differences between EN 16258 and ISO 
14083, e.g. with regard to system boundaries and terms, 
in tabular form. The glossary of key terms at the 
beginning of this guide reproduces parts of Annex S. 
1.2 Terms and basics 
GHG emissions from transport processes come from 
various sources. For this reason, ISO 14083 
introduces corresponding terms to differentiate GHG 
emissions, as the previously common terms such as 
well-to-tank (WTT), tank-to-wheel (TTW) and well-
to-wheel (WTW) are already used in other standards 
and are not suitable for hub-specific processes. The 
new term energy provision GHG emissions refers 
to the release of greenhouse gases during the 
production, storage, processing and distribution of 
energy carriers (including electricity) for use in 
transport chains. It replaces the terms indirect or 
WTT emissions. Operation GHG emissions on the 
other hand, refer to the release of greenhouse gases 
due to the operation of vehicles or hubs, replacing the 
former direct or TTW emissions. They are caused by 
the combustion or leakage of fuels and the leakage of 
refrigerants. GHG emissions from energy provision 
and operation are combined into total GHG 
emissions. In addition, the standard also uses the 
term Packaging life cycle GHG emissions. 

---

## Page 12

12 
 
 
Overview  
 
 
 
This includes all GHG emissions generated during the 
life cycle of (transport) packaging that is used, for 
example, at hubs for the (re)packaging of freight and 
can be optionally taken into account. 
 
To put these terms and emissions in the context of 
transport, ISO defines a transport chain as a 
sequence of elements that are associated with the 
carriage of passengers and freight from a point of 
origin to a place of destination. The elements of a 
transport chain within which passengers or cargo 
are transported by a vehicle or transferred through 
a location (hub) are referred to as transport chain 
elements (TCEs). ISO 14083 uses the term vehicle 
to encompass all means of transport. 
This is used in this document as an umbrella term for 
all modes of transport. 
 
In order to group transport operations or transport 
chain elements that share similar characteristics, so-
called transport operation categories (TOCs) are 
used (see ISO 14083 Section 3.1.29). These include, 
for example, the consideration of different vehicles or 
passengers or freight types and different levels of 
granularity. For example, a TOC can be formed for a 
vehicle on a specific route, but also for a group of 
vehicles in a network. If a vehicle transports people 
and freight at the same time, for example, the 
associated TOC may contain several TCEs with 
different GHG emission intensities (see ISO 14083 
Section 6.3). 
 
 
 
Figure 2 
 
Example of a transport chain of freight with possible transport and hub operation categories  
Source: own illustration based on ISO 14083 Figs. 6 and 7 
 


---

## Page 13

13 
 
 
Overview  
 
 
 
A similar term is used for transport chain elements 
that describe hub processes. Hub Operation 
Categories (HOCs) are defined as a group of hub 
operations that share similar characteristics (see ISO 
14083 Section 3.1.12), such as processes, cargo type, 
or ambient temperature/temperature control. These 
include, for example, the temperature control of goods 
and air conditioning for passengers. A HOC must fully 
encompass each hub operation, so typically one or 
more hubs are considered as a whole. Details on 
individual cases in which a hub can be assigned to 
multiple HOCs are described in section 4.1.2. 
 
In order to be able to calculate GHG emissions for 
these operation categories, the relevant activities of 
processes that cause GHG emissions are analysed and 
the necessary data is collected. This data is called GHG 
activity data. The GHG activity data for transports 
and hubs generally refer to the use of fuels, other 
energy consumption, the leakage of refrigerants and, 
optionally and in the case of hubs, to the use of 
transport packaging material. The assessment shall 
include all relevant greenhouse gases. In transport 
chains, the most relevant greenhouse gases are 
usually (fossil) carbon dioxide (CO2), methane (CH4), 
nitrous oxide (N2O) and climate-relevant refrigerants, 
e.g. R-452a, R-404A or R-134a. Further information 
can be found in the reports of the United Nations 
Intergovernmental Panel on Climate Change (IPCC) 
(IPCC 2023). 
 
All reported GHG emissions are expressed in carbon 
dioxide equivalents (CO2e). Here, the so-called Global 
Warming Potential (GWP) comes into play. The GWP 
reflects how much a greenhouse gas contributes to 
global warming in relation to carbon dioxide over a 
chosen time horizon (usually 100 years). These 
conversion factors are continuously published by the 
IPCC in reports: the latest is the Sixth Assessment 
Report (Smith et al. 2021). 
 
Once GHG activity data has been collected and GHG 
emissions have been calculated using appropriate 
GHG emission factors, GHG emission intensities can 
be calculated  
taking into account transport activities or hub 
activities. Transport activity should be expressed in 
either tonne-kilometres (tkm) or passenger-
kilometres (pkm), so that GHG emission intensities 
for transport can be calculated using the amount of 
GHG emissions per tkm or pkm. The GHG emission 
intensities for hubs are described using the hub 
activity as throughput in tonnes or passenger 
transfers, so that the GHG emission intensities for 
hubs per tonne or per passenger can be calculated. 
 
These key figures are suitable for internal purposes, 
e.g. for setting emission intensity targets, as well as 
for exchanging information with customers or 
shippers for ISO-compliant transport chain 
calculations. 
 
The next sections provide a precise procedure for the 
greenhouse gas calculation according to ISO 14083 
and further information on the central basics. 
1.3 Guide to the guide –  
Where can you find what? 
The guideline serves as a guide for the application of 
ISO 14083 and begins with some basics of the 
required procedures: 
▸ The most important basics are summarised in 
Section 2.1: What needs to be considered with 
regard to system boundaries? Which processes 
must be considered and which will not? Since hubs 
are now mandatory (normative) compared to EN 
16258, what are the system boundaries for hubs? 
 
▸ What should be considered in principle with regard 
to data quality and data categories used for GHG 
emission calculations? Answers are given in 
Sections 2.2 and 4.2.3. 
 
▸ Section 2.3 presents the procedure for calculating 
GHG emissions in accordance with ISO 14083. 
 
The further structure of the guideline is based on the 
steps of a GHG emission calculation of transport 
chains, which are described individually and 
explained with examples. 

---

## Page 14

14 
 
 
Overview  
 
 
 
▸ Chapter 3 describes how a defined transport chain is 
divided into transport chain elements and how the 
transport or hub activity of the transport chain or the TCE 
is calculated. In this chapter, the case examples (Part 1) 
are also presented and the first steps of a GHG emission 
assessment are applied as examples. 
 
▸ Chapter 4 focuses on data collection and GHG emission 
calculations: it describes how transport and hub 
operations categories (TOCs, HOCs) are established (see 
Section 4.1).  
 
▸ How the determined consumption data are converted 
into GHG emissions and, based on this, GHG emission 
intensities are calculated, is explained in Section 4.2. 
What are GHG emission factors and where can I find the 
appropriate values (see Section 4.2.1)? How are 
emissions allocated in accordance with the standard and 
when is this necessary at all (see Section 4.2.2)? And, 
somewhat more detailed than in Chapter 2: What exactly 
are primary data, what are secondary data and when can 
the latter be used (see Section 4.2.3)? Insights on 
refrigerant types and potential losses can be found in 
Section 4.2.4. 
 
▸ Part 2 of the case examples rounds off Chapter 4: It is 
shown by way of example how TOCs and HOCs are 
selected for the defined transport chains, data is assigned 
and GHG emissions and the associated emission 
intensities are calculated. 
 
▸ Chapter 5 explains how the interim results obtained for 
the TOCs and HOCs can be applied to the GHG emissions 
calculation of the entire transport chain. Part 3 of the 
case examples illustrates the application of the explained 
concepts.  
 
▸ Chapter 6 presents the reporting requirements 
according to ISO 14083. Examples of reports are 
presented in the case examples in Part 4.   
 
▸ Finally, the Annex sets out relevant GHG emission factors 
that are taken into account in the GHG emission 
calculation or reference is made to sources for other 
factors. 
It should be noted at this point that the abbreviations 
used usually refer to the English terms of ISO 14083. 
For example, TCE stands for transport chain element 
or TOC for transport operation category. For this 
reason, the glossary at the beginning of the guide 
contains the technical terms as well as the 
abbreviations and a short explanation or reference to 
the corresponding chapter. 
 
Case examples in this guide  
The guide offers two central case examples, for which 
the calculation of GHG emissions is described step by 
step and which are taken up and continued in the 
chapters. For selected questions, further examples 
complement the explanations to highlight details 
separately. 

---

## Page 15

15 
 
 
 
2 Basic procedure 
 
In addition to transparency, a central principle of any 
greenhouse gas accounting is the application of a 
uniform and consistent methodology based on correct 
data. In case of doubt, a conservative approach should 
always be chosen and, in the case of several 
accounting options, a uniform approach should 
always be chosen within one calculation and report 
that is presented in a clear and transparent way. It is 
also important to select the reporting period 
correctly. According to ISO 14083, periods of up to 
one year are permissible here in order to be able to 
compensate for possible short-term or seasonal 
fluctuations. In certain cases, shorter periods need to 
be taken into account, e. g. if a bus used for passenger 
transport of tourists only runs during a certain time of 
the year. Completeness of the calculation is also key: 
no greenhouse gases or processes causing GHG 
emissions must be omitted, and if the total emissions 
are divided among passenger or freight groups, the 
total sum of the individual GHG emissions must 
always be equal to the calculated total. 
2.1 Basics of assessment and system 
boundaries 
ISO 14083 prescribes which processes must be 
included in a calculation, can be included and which 
must not be included. Of course, it is optional to add 
other non-included processes, but this is done outside 
of the ISO 14083-compliant calculation and must be 
reported separately.
 
2.1.1 Which processes must be considered? 
Included processes  
All transport operations by air, cable car, inland 
waterway, pipeline, rail , road and sea transport, as well 
as all hub operations within the transport chain  must 
be included. Here, all parts of a transport chain in 
which GHG emissions are generated by the use of 
energy carriers or refrigerants must be included. All 
GHG-emitting activities due to loaded and empty trips 
(including diversionary and/or out-of-route distance) 
as well as start/stop and idling processes and operation 
of all propulsion or auxiliary engines must be included. 
 
This must include, in particular: 
▸ GHG emissions from vehicle or hub operation through 
fuel combustion or leakages and losses of refrigerants 
▸ GHG emissions from the provision of all energy 
carriers used, including electricity, over their entire life 
cycle (including energy infrastructure) 
2 Basic procedure 

---

## Page 16

16 
Basic procedure 
 
 
 
 
In addition to the processes included, ISO 14083 
also enables several optional processes: 
(re)packaging processes, storage of freight, use of 
information and communication technology, and 
black carbon emissions. 
 
It is important that no processes or emissions are 
omitted from the quantification unless this is clearly 
indicated by a cut-off criterion within the reporting. 
To this end, a justification must be provided as to 
why a cut-off criterion is necessary and permissible. 
For example, it can be shown that the calculation 
result is not changed as a result. A cut-off criterion 
can refer to a certain percentage of transport or hub 
activity or energy consumption of the transport 
chain, or to a certain percentage of GHG emissions. In 
doing so, the ISO 14083 does not give information on 
the height of this cut-off criterion. However, care 
should be taken to ensure that the cut-off criterion 
and its height are chosen in such a way that the 
statement is not changed in a comparison between 
two similar transport chains. 
 
An example of the application of such a cut-off 
criterion is the consideration of infrastructure in the 
GHG emissions of energy provision. For example, it 
has been shown that in the case of fossil fuels, 
infrastructure is responsible for less than one 
percent of total GHG emissions (i.e. the sum of GHG 
emissions from operation and GHG emissions from 
energy provision) (John Beath et al. 2014). This 
means that this one percent of GHG emissions can be 
used as a cut-off criterion if the data used for the GHG 
emission factors of fossil fuels do not take into 
account the infrastructure. 
 
Processes not included  
Importantly, ISO 14083 is used to quantify the 
reporting body's real GHG emissions over a period of 
time. This means that it is prohibited to include the 
results of emission trading measures or offsetting. 
 
In addition, the following processes according to ISO 
14083 are not part of the quantification: 
▸ Manufacture, maintenance and scrapping of 
vehicles as well as transport and hub 
infrastructure 
▸ Production of refrigerants 
▸ Processes at the administrative (overhead) 
level of the transport service providers 
▸ Waste 
▸ Businesses co-located in a hub (e.g. retail 
and hospitality services) that are not 
needed to operate the hub 
 
2.1.2 Hub-specific system boundaries 
Hubs are their own transport chain elements. Since 
these were not included in the previous EN 16258, 
they will be presented in more detail below. The 
boundaries for assessing GHG emissions from hubs 
starts when 
▸ the shipment is unloaded from the incoming 
means of transport, or 
▸ the passenger disembarks from the incoming 
means of transport or begins their journey at the 
hub. 
 
It ends when 
▸ the consignment is either handed over to the 
recipient or reloaded onto the outgoing means of 
transport, or 
▸ the passenger boards the next means of transport 
or ends their journey at the hub. 
 
The system boundaries of the ISO refer to 
transhipment processes (freight) or transfer 
processes (passengers) that require energy or release 
refrigerants. Comparable storage and (re)packaging 
processes for freight are optional; the standard does 
not specify a precise definition of dwell time to 
categorise hubs as transhipment or storage sites, as 
this depends heavily on the respective industry. It 
also often happens that part of the freight is 
transhipped directly at one hub, while another part of 
the freight is (temporarily) stored, so that in this case 
it may be necessary to split the respective emissions. 
How a hub can be narrowed down and how related 
HOCs can be defined is explained in Section 4.1.2. 

---

## Page 17

17 
 
 
Basic procedure  
 
For a more detailed limitation of the GHG emission 
calculation, the following compilation of the 
processes to be included and excluded for hubs is 
used. The respective possible GHG-emitting 
processes or equipment are described and 
illustrated with examples. Whether they are 
normatively within the system boundaries of hubs 
("yes"), excluded ("no") or considered an optional 
aspect ("optional") is explained in the right-hand 
column. 
 
Table 1 
 
Hub operations to be included (yes), excluded (no) and optional in the GHG emissions calculation 
Description Examples yes/no/ 
optional 
Vehicles and other equipment for the 
transport, movement and handling of 
cargo or passengers 
Industrial trucks, automated guided 
vehicles (AGVs), conveyor belts, shuttle 
systems, cranes, reach stackers, 
escalators, elevators, apron buses, 
shuttle boats 
yes 
Vehicles and equipment for the shunting of 
vehicles/ships, trailers, containers on the 
hub’s premises (see note 1) 
Converter, push boats, pilot/tow boats, 
shunting locomotives, aircraft tractors (in 
so-called aircraft dispatch towing 
procedure, aircraft pushback, tow tractor) 
yes 
Transport of employees at roll-on-roll-off 
terminals who steer the self-propelled 
vehicles to be transhipped 
Shuttle vehicles yes 
Drive energy of self-propelled vehicles used 
for loading (i.e. driving to or from the 
means of transport*)  
Cars, tractors, trucks no 
Technical building equipment of the hub Lighting, heating, air conditioning yes 
Handling of baggage carried by passengers 
is part of a passenger transfer 
Check-in counters, baggage carousels, 
cargo tugs 
yes 
Handling of pre-shipped baggage is part of 
cargo transhipment (see note 2) 
yes 
Information and communication technology 
(ICT) services through hub infrastructure 
Server rooms, data centres, cloud services yes 
ICT services purchased from external server 
providers 
optional 
Commuting to/from the hub of the hub Commuter traffic no 
Transport of crew members of 
vehicles/vessels of inbound or outbound 
transport 
Drivers, train drivers, train attendants no 
Shopping malls, restaurants, hotels located 
at the hub 
Shopping centres, restaurants no 
Equipment for the storage of goods Stacker crane, high-bay warehouse, small 
parts warehouse 
optional** 
* e.g. car train, ferry, ship 
** The original German version of this guide contains an error here where it should read “optional” instead of “no”. This error has been 
corrected in this version. 

---

## Page 18

Basic procedure 
18 
 
 
 
Note 1: This refers to processes inside and outside 
buildings. If a vehicle or equipment is used between 
two terminals, as is conceivable at a seaport, for 
example, the energy consumption must be allocated to 
one or both terminals on a pro rata basis. However, 
the assigning rule must be applied consistently. 
 
Note 2: While baggage carried by passengers can be 
clearly assigned to passenger transport, baggage that 
is transported by a logistics service provider 
independently of a person's actual journey (and the 
course of travel) is baggage shipment and thus goods 
transport. 
 
In addition to the GHG-emitting operations 
mentioned above, other operations that occur 
geographically in hubs must be included in the GHG 
emission calculation in accordance with ISO 14083 
(see Table 2). However, the ISO recommends that 
these GHG emissions should not be assigned to the 
hubs, but that they should be taken into account as 
part of the transport chain elements for transport. 
 
The ISO recommends that the GHG emissions 
associated with this consumption is assigned to 
upstream or downstream transport TCEs. However, 
if the reporting organisation assigns them to the hub, 
this must be applied consistently. 
 
Table 2 
 
GHG emissions of  operations at hub premises that 
should be assigned to inbound or o utbound transport 
Description  Examples 
 
Energy use of 
vehicles/ships that 
temporarily stay in the hub 
 
Auxiliary/main 
engines, ground 
power unit, shore 
power 
 
Energy use of vehicles of 
incoming or outgoing 
transport on the hub 
premises, incl.  refuelling, 
or charging of electrically 
powered transport means 
at the hub or refilling of 
refrigerants in vehicles, 
superstructures, reefer 
containers 
 
Vehicles, ships, 
airplanes, trains 
 
 
In the future, clearer specifications will have to be 
developed in order to avoid gaps in the assessment of 
the transport chain and to create further consistency 
in the calculation of emissions along the transport 
chains. In the future, both the GHG Protocol and 
Incoterms1 may form the basis for assignment rules. 
2.2 Data quality and data categories 
An important basis for any GHG emissions calculation 
is the selection and collection of appropriate and high-
quality data. Regardless of which step of the 
calculation a quantification is needed, it is important 
that data are used that are representative of the 
transport chain (elements) under consideration and 
that fit geographically as well as in terms of time and 
technology, in order to obtain a meaningful result. 
 
According to ISO 14083, there are basically two 
different types of data that are used in the calculations: 
primary data, which result directly from a 
measurement (or are calculated on the basis of 
measured values), and secondary data. In the case of 
secondary data, a distinction is made between 
modelled data and default data. In principle, ISO 14083 
prescribes the use of primary data specifically 
determined for the transport chain. Only if such 
primary data is not available, secondary data may also 
be used, provided that a justification is provided. In 
this context, modelled data is to be given preference 
over the use of default values. 
 
The report must show which data types were used for 
what and why. Since many transport service providers 
do not have (complete) operational or financial control 
over the entire transport chain, the use of pure 
primary data is often limited in reality, and many 
calculations will be based on a mixture of different 
data types. 
 
In principle, the mere indication of the extent to 
which primary or secondary data has been used does 
not make it possible to assess the quality of the data. 
Although further information on data quality 
 
 
 
1 International trade clauses 
 
 

---

## Page 19

19 
 
 
Basic procedure 
 
would be desirable, ISO 14083 does not stipulate any 
requirements in this regard. One possible quality 
criterion could be the granularity of the TOC or HOC 
used: the more specifically, for example, the 
transports are grouped together according to 
purpose/route and vehicles used (e.g. the same 
vehicles/vehicle types, combination of a group of 
similar vehicle types in certain regions and routes), 
the more specific the assessment and thus probably 
higher the data quality. According to the authors, 
secondary data derived from specific modelling 
(which in turn uses high-quality primary data as 
input data) can be used to generate comparable 
quality of GHG emission calculation such as  
 primary data (i.e. measurement data) – provided that 
all parameters relating to GHG activities are 
sufficiently taken into account. 
 
2.3 Introduction to step-by-step GHG emissions 
calculation 
Every greenhouse gas calculation according to ISO 
14083 must be carried out in six steps, whereby the 
specific procedures in the individual steps differ 
depending on the case under consideration. The 
basic procedure is as follows: 
 
Figure 3 
 
Steps to calculate GHG emissions for a transport chain    
Source: own illustration, ifeu/Fraunhofer IML, based on ISO 14083 
Secondary 
data 
 


---

## Page 20

Basic procedure 
20 
 
 
 
 
▸ Step 1: Definition of the transport chain and 
breakdown into individual transport chain elements 
▸ Step 2: Identification of the related transport/hub 
operations 
▸ Step 3: Grouping of transport/hub operations into 
transport/hub operation categories 
▸ Step 4: Calculation of GHG emission intensities at 
TOC/HOC level based on transport/hub activity and 
GHG emissions of TOCs/HOCs 
▸ Step 5: Calculation of the GHG emissions of the TCEs 
based on the transport/hub activity of the TCEs and 
the GHG emission intensity of the related 
TOCs/HOCs 
▸ Step 6: Calculation of the GHG emission 
intensity of a transport chain from the sum of 
the GHG emissions of the individual TCEs and 
the transport activity at the transport chain level 
 
Figure 3 visualises this flow diagram. 
 
In the following chapters, the individual calculation 
steps are discussed in more detail: steps 1 and 2 are 
described in more detail in Chapter 3, steps 3 and 4 
in Chapter 4 and steps 5 and 6 in Chapter 5, clearly 
explained using two case examples. 
 
Figure 4 
 
Which steps are described in which chapter? 
 
 
 
 
   
Source: own illustration, ifeu/Fraunhofer IML, based on ISO 14083 


---

## Page 21

21 
 
 
 
3 Transport chain elements and activity data 
 
3.1 Breakdown of the transport chain into 
transport chain elements 
At the beginning of the GHG emissions calculation, the 
relevant transport chain is defined, whereby the 
requirements for system boundaries listed in Section 
2.1 must be considered. A transport chain describes 
the transport of freight or people from a point of 
origin to a destination. It can be divided into a 
sequence of individual transport chain elements 
(TCEs), each of which describes a section of the 
transport chain (e.g. a freight transport with a certain 
type of vehicle on a section of the entire transport 
chain). ISO 14083 leaves open whether the transport 
chain begins and/or ends with a hub TCE (e.g. a 
finished goods warehouse). This is at the discretion of 
the reporting organisation. 
3.2 Calculation of the transport and hub 
activity of the transport chain elements 
Each transport chain element has a corresponding 
transport or hub activity. This describes and 
quantifies the associated transport or hub operation 
for a certain number of passengers or quantity of 
freight. 
3.2.1 Transport activity and transport activity 
distance 
First, the associated transport activity is determined 
for the individual transport chain elements. 
 
 
 
 
 
 
 
 
 
 
 
 
 
This refers to a certain number of passengers or 
quantity of freight transported over a certain 
distance. 
 
In the case of passenger transport, the transport 
activity is expressed in passenger-kilometres (pkm) 
and is calculated as follows: 
 
Number of passengers x transport activity distance 
 
In the case of freight transport, the transport 
activity is determined by the quantity of freight 
transported (i.e., actual freight mass including the 
original packaging, but without additional transport 
packaging used by the forwarder, such as pallets 2 or 
container) and the distance. It is usually expressed 
in tonne-kilometres (tkm) and is calculated as 
follows: 
 
Freight mass x transport activity distance
 
2 If different cargo items on a pallet are consolidated and packed by the shipper (e.g. by shrink wrap), then this is considered as one consignment and 
thus the pallet as a component of the load. 
 
 
3 
Transport chain 
elements and 
activity data 


---

## Page 22

22 
Transport chain elements and activity data  
 
 
 
In certain cases, the freight mass can also be the mass 
of empty containers or pallets, if the purpose of the 
transport is to transport them. In addition, other units 
such as TEU or number of items (for mail and parcel 
operations) can also be used in justified cases. 
 
To determine the transport activity, the 
corresponding transport activity distance is 
required in each case, i.e. the distance travelled by 
the freight or passenger. 
 
According to ISO 14083, two types of distance are 
generally permitted: the great circle distance (GCD) 
and the shortest feasible distance (SFD).  
 
The great circle distance (GCD) is the shortest 
distance between two points on the earth's surface 
along the globe. The shortest feasible distance (SFD) is 
the shortest suitable route, taking into account the 
infrastructure options for a given vehicle type. Smaller 
detours, for example to avoid traffic jams in city 
centres or to avoid certain road types for particularly 
large vehicles, can already be included. 
 
In order to enable comparability of the values between 
different providers of transport services, the use of a 
uniform distance is important. In principle, all 
transports must be calculated either with the GCD or 
with the SFD. Air transports should always use GCD. 
For road, rail, cable cars, pipelines and water, either the 
SFD or the GCD should be used, whereby the type of 
distance used must be clearly stated and mixtures are 
not permitted. In practice, the use of SFD is probably 
more relevant for all transports except air transport, as 
it is much closer to the real distance. 
 
In order to obtain correct and realistic calculation 
results, the distance on which the GHG emission 
intensity is based and the distance underlying the 
calculation of the transport activity must always be 
the same. 
If only the actual distance is available, a distance 
adjustment factor (DAF) is required to determine the 
transport activity distance. This describes the 
relationship between actual distance and transport 
distance. With a distance adjustment factor of 1.05, 
this means that the actual distance is 5 percent longer 
than the shortest feasible distance3. 
 
The annexes to ISO 14083 list the type of distance and 
possible distance adjustment factors for each means of 
transport. In the case of rail transport, inland 
waterway vessels, pipeline transports and cable cars, 
it can be assumed that the actual distance corresponds 
to the shortest feasible distance, as the specified 
transport route network (e.g. rail infrastructure or 
waterway network). Common adjustment factors for 
air, road or sea transport are shown in Table 3. 
 
Even in the case of collection and delivery rounds, 
either the GCD or the SFD must be used as the distance 
between the respective loading and unloading points. 
In this case, the distance is not based on a real route, 
but merely represents a fictitious distance between 
the loading and unloading points, by means of which 
the total emissions of the tour are apportioned to the 
individual consignments, using the tonne-kilometres 
calculated with the fictitious distance. 
 
Example 5 in Section 4.2.2 illustrates the GHG emission 
calculation of a collection and delivery rounds. The use 
of a distance adjustment factor in road transport is 
shown in Case example A. 
3.2.2 Hub Activity 
 
To calculate the GHG emission intensity of hubs, the 
hub activity is required. This is the quantity of freight 
or the number of passengers leaving a hub. For freight 
handling, the standard unit is "tonne," although in 
justified cases, such as with transport activity, 
alternative units like TEU or the number of shipments 
(for postal and parcel operations) may be used.
 
 
 
 
3 This is important for a comparable GHG emission calculation in two respects: When calculating GHG emissions based on real distances, the distance 
travelled should not be underestimated (because GHG emissions must also include detours, etc.). When determining the GHG emission intensity, in turn, 
the transport activity distance should not be overestimated in order to allow a fair comparison. 
 
 

---

## Page 23

23 
 
 
Transport chain elements and activity data   
 
Table 3 
Distances and distance adjustment factors  
Modes Examples Distance adjustment factor Actual distance 
Air transport GCD  GCD + 95 km 
Road transport SFD 1.05 SFD + 5 % 
Maritime transport SFD 1.15 SFD + 15 % 
Source: ISO 14083  
3.3 Case examples Part 1 
The guide will illustrate the step-by-step calculation 
process using two (greatly simplified) fictitious case 
examples. In the following, both case examples are 
briefly presented, and the first two calculation steps 
are followed. 
The calculations in the case examples represent 
fictitious cases, the quantification of which is based on 
the most realistic boundary conditions possible. 
Nevertheless, the GHG emissions and GHG emission 
intensities calculated in this way are only to be seen as 
examples and serve to illustrate the calculation 
processes. Moreover, the procedure does not claim to be 
complete. In order to address typical peculiarities and 
questions in the GHG emission calculation of transport 
chains in parallel to the examples, the case examples 
are supplemented by individual examples, which in turn 
do not always reflect the level of detail required by ISO 
(e.g. differentiation of GHG emissions due to operation 
and energy provision). 
 
Example A: Transport services in freight transport  
 
A company wants to quantify and report GHG emissions for a specific freight transport service.  
 
The transport service is the transport of containerised average goods at ambient temperature, which is to be 
transported from point A to point B in Germany. The means of transport used in the pre -carriage and onward 
carriage are a modern articulated truck with diesel drive in combined transport 4(CT). The main leg is realised by rail 
with an electrically powered freight block train with containers (TEU).  
 
The company has neither financial nor operational control over the transports carried out and therefore has no 
primary data for the GHG-emitting activities. However, it knows the route and the freight mass (including the 
packaging originally supplied), which is 10 tonnes, and asks the companies carrying out the transport operations for 
further data. Since the transport service involves the use of different modes of transport, the hub operations at an 
intermodal terminal, i.e. the transfer of the container to the train and vice versa, must also be taken into account.  
 
 
4 In combined transport, goods are transported using different means of transport without changing the load carrier (in this case a container). Although 
articulated trucks are normally allowed to weigh a maximum of 40 tonnes, total weights of up to 44 tonnes are permitted in combined transport. 
 
 

---

## Page 24

Transport chain elements and activity data  
24 
 
 
 
Figure 5  
 
Illustration of steps 1 and 2: Transport chain elements  
 
 
Source: own illustration, ifeu/Fraunhofer IML 
 
Step 1: Breakdown of the transport chain into individual transport chain elements (TCEs)  
 
In the first step, the transport chain is broken down into the individual transport chai n elements after it 
has been defined. These are: 
▸ TCE 1: Road transport 
▸ TCE 2: Transhipment at CT Terminal A 
▸ TCE 3: Transport by train 
▸ TCE 4: Transhipment at CT Terminal B 
▸ TCE 5: Road transport 
 
Figure 5 visualises the transport chain and its transport chain elements. 

---

## Page 25

25 
 
 
Transport chain elements and activity data  
 
 
 
Step 2: Identifying the TO/HO for each TCE  
In the second step, the relevant transport or hub operation is identified for each transport chain 
element and the associated transport or hub activity is calculated.  
 
The two road transports in TCE 1 and TCE 5 are each carried out by a diesel articulated truck in 
combined transport. For these, the respective transport activity distances are required. For the pre -
carriage (TCE 1), the company determines a shortest feasible distance (SFD), taking into account the 
transport network of 50 km, and for the on-carriage (TCE 5) an SFD of 100 km. Since the vehicle 
consumption was determined for actual distances travelled, a distance adjustment factor is used to 
calculate the GHG emissions of the articulated truck in step 3. The company uses the 5% surcharge on 
the SFD recommended in the ISO for this purpose. 
 
Rail freight transport is carried out by an electrically powered freight train. An inquiry with the railway 
company reveals that the freight train covers a distance of 500 km between the loading and unloading 
of the container in question. Since the actual distance of a train usually does not deviate from the 
shortest feasible distance, no distance adjustment factor has to be used here. Only the freight mass of 10 
t in the container counts as mass here, as the container dead weight of 2.25 t influences the e nergy 
consumption of the transport, but is not counted as freight mass.  
 
This results in the following transport/hub activities: 
 
▸ Transport activity for TCE 1: 50 km x 10 t = 500 tkm (SFD) or 525 tkm (actual distance) 
▸ Hub activity for TCE 2: 10 t 
▸ Transport activity for TCE 3: 500 km x 10 t = 5,000 tkm (SFD) 
▸ Hub activity for TCE 4: 10 t 
▸ Transport activity for TCE 5: 100 km x 10 t = 1,000 tkm (SFD) or 1,050 tkm (actual distance) 
 
 
 
Example B: Passenger transport of an organisation  
 
In the second case example, a calculation according to ISO 14083 is carried out for an organisation that 
wants to calculate GHG emissions of its provided passenger transport during a calendar year. 
 
In this case, it is a bus company that operates in local transport and maintains its own vehicle fleet. This 
fleet consists of a total of 21 buses: including 2 articulated buses with electric drive, 14 articulated 
buses with diesel drive and 5 standard diesel buses. The diesel busses are of different age and therefore 
partly have different emission classes. The electric buses are charged exclusively at the bus depot of the 
organisation. The company has primary data on the annual driven distance of the busses as well as for 
fuel and electricity consumption. The bus occupancy is also based on primary data , however the 
company uses collected data from passenger counts for selected lines and times. Care was taken to 
ensure that the data included various weekdays and times so that the average occupancy rate of the 
buses is as reliable as possible. The company now wants to publish an annual report on the GHG 
emissions from passenger transports it has carried out. 
  

---

## Page 26

Transport chain elements and activity data  
26 
 
 
 
 
 
 
Step 1: Breakdown of transport chain(s) into individual transport chain elements (TCEs)  
In this case example, the sum of all transport chains carried out by the bus company, i.e. the use of all 
buses for passenger transport, is used. A separate transport chain element is defined for each individual 
bus of the company, which includes the transport service provided within one year.  
 
For clarity, similar TCEs are summarised here: 
▸ TCEs 1 to 12: Bus no. 1 to no. 12 (articulated buses, diesel, purchased between 2015 and 2018) 
▸ TCEs 13 and 14: Bus no. 13 and no. 14 (articulated buses, diesel, purchased in 2022) 
▸ TCEs 15 and 16: Bus no. 15 and no. 16 (articulated buses, electric) 
▸ TCEs 17 to 20: Bus no. 17 to no. 20 (standard bus, diesel, purchased in 2017) 
▸ TCEs 21: Bus no. 21 (standard bus, diesel, purchased in 2013) 
Step 2: Identifying the TO/HO for each TCE  
Now the corresponding TO and the transport activity (in passenger -kilometres) are determined for 
each TCE. The organisation can access primary data for the individual buses. 
 
To determine the TO, the properties of the buses purchased in different years are determined. In 
particular, it shows that the diesel buses sometimes have different emission classes.  
 
Here, too, similar TO are listed together: 
 
▸ TO of TCEs 1 to 12: articulated buses, diesel, Euro 6a-c 
▸ TO of TCEs 13 and 14: articulated buses, diesel, Euro 6d 
▸ TO of TCEs 15 and 16: articulated buses, electric 
▸ TO of TCEs 17 to 20: standard bus, diesel, Euro 6a-c 
▸ TCE 21: standard bus, diesel, Euro 5 
 
Since the primary data for the distances travelled are not based on the actual mileage of the buses, but 
on the planned routes, the distance corresponds to the shortest feasible distance in each case. In doing 
so, the organisation makes sure that it does not use the planned timetables, but the actual schedules. 
Thus, detours or other journeys that are not related to the transport service provided are included in 
fuel consumption, but they do not count as transport activity. In  order to calculate transport activity, the 
capacities of the buses (seats) and the average occupancy rate of 18 per cent are also required. For the 
sake of simplification, a list of all individual transport activities is omitted here and only the calculation 
is briefly outlined as an example for a single TCE. 
 
▸ Transport activity of TCE 1: 55,0000 km/a  x  90 seats  x  0.18 = 819,000 pkm/a  
 
Similarly, the transport activities of the other TCEs can also be calculated.

---

## Page 27

27 
 
 
 
4 Getting started with calculation and data collection 
 
4.1 Establishment of transport and hub 
operation categories 
In order to simplify calculations and data collection, it 
makes sense to group comparable transport or hub 
operations into so-called transport/hub operation 
categories (TOCs/HOCs). Operations with similar 
characteristics (e.g. in terms of vehicle type, number 
of vehicles, route, freight type) over a fixed period of 
time (up to one year). 
 
Each transport chain element with its associated 
transport or hub activity is then assigned to a 
transport or hub operation category to facilitate data 
collection and quantification. 
 
The identification of the transport/hub activity of a 
TOC or HOC is analogous to that of a single transport 
chain element. 
 
4.1.1 Transport operation category 
Each individual transport operation (and thus also 
the individual transport chain elements) must 
always be considered in the context of the entire 
system. Transport operation categories (TOCs) are 
therefore used to group transport operations with 
similar properties over a certain period of time (of 
up to a calendar year). 
 
 
TOCs are influenced by the following factors: 
▸ Number and type of vehicles as well as special vehicle 
features 
▸ Type of cargo and necessary conditions during 
transport (e.g. refrigeration) 
▸ Period 
 
The individual TOCs can have different granularity. 
Thus a TOC can be applied to 
▸ a specific vehicle on a specific route, 
▸ a specific vehicle on different routes, 
▸ a specific type of vehicle on a specific route, 
▸ a certain type of vehicle on different routes, 
▸ a group of vehicles on a specific route, 
▸ a group of vehicles on different routes. 
4 
Getting started with 
calculation and 
data collection 


---

## Page 28

28 
Getting started with calculation and data 
collection 
 
 
 
 
It is quite possible that vehicles with different 
drivetrains or fuels are grouped in the same TOC. 
 
However, a single transport operation may not be 
divided into several TOCs, even if two different 
transport chain elements are involved. (e.g. freight and 
passenger transport). 
 
Transport operation categories are divided into 
different basic types, each of which differs in its 
method of calculation. In general, it is divided into 
▸ passenger-only TOCs (general or subdivided into 
different passenger classes), 
▸ freight-only TOCs (general or subdivided according 
to different temperature levels), 
▸ mixed freight and passenger TOCs, and 
▸ other TOCs. 
 
Depending on the type of TOC, an allocation (see 
Section 4.2.2) may be necessary. 
 
It is important that a TOC should always cover the 
entire round trips (i.e. journeys with different loading 
levels, including empty runs as well as outward and 
return journeys) in order to balance out GHG emissions 
within asymmetric transport operations. 
 
To facilitate the establishment of meaningful TOCs, ISO 
14083 provides an overview of the possible 
characteristics in each of the mode-specific annexes on 
the basis of which the establishment can be made. In 
addition to these more general requirements, 
additional specific factors can also be included, such as 
the topography, the type of route, the vehicle size, 
other information about the vehicle or the emission 
classes. Further information on the different modes of 
transport and their TOC characteristics can be found in 
Annex A.2. 
 
4.1.2 Hub operation category 
On the one hand, hubs can include entire locations, such 
as distribution centres, 
combined transport terminals or a metro station. On 
the other hand, they can be self-contained facilities 
within a larger infrastructure of passenger or 
freight transport, as is the case with airports, 
seaports, ferry ports or larger railway stations, for 
example. Here, several hubs (e.g. terminals for liquid 
goods and containerised cargo) are often located in 
one location, operated by different companies, and 
the relevant hub (or hubs) should be distinguished 
as a separate entity from other services and  
facilities5.For example, individual terminals at a 
seaport can each be separate hubs (e.g. container 
port, roll-on-roll-off terminal, liquid bulk terminal), 
just as an airport can include hubs for passenger 
transport (various passenger terminals, regional or 
long-distance railway stations) as well as different 
freight terminals of individual logistics service 
providers for cargo transhipment. 
 
Basically, a HOC must fully encompass every hub 
operation. So, if a GHG-emitting activity serves 
several processes (e.g. industrial trucks move 
different freight groups), these processes and their 
consumption must be grouped in a HOC. If the 
activities as a whole serve different processes, they 
can be defined as separate HOCs of a hub. 
 
If a hub includes several different hub operations (e.g. 
cold warehouse lighting, dry warehouse lighting, 
cooling, industrial trucks), of which 
▸ one part (e.g. cold warehouse lighting, dry warehouse 
lighting, cooling) completely serves two different 
processes, e.g. 
▸  storage of refrigerated goods (cold warehouse 
lighting, cooling) or 
▸ storage of ambient goods (dry warehouse lighting), 
▸ one part (e.g. industrial trucks) serves, however, both 
(storage of refrigerated and ambient goods), 
 
this hub is to be regarded as one HOC. Also, a hub can 
serve freight groups of different seasons. 
 
 
5 This partly deviates from the usual language and use of the term "hub". Accordingly, sea and inland ports, for example, are often referred to as hubs. 
 
 

---

## Page 29

29 
Getting started with calculation and data 
collection 
 
 
 
In this example, the hub with its respective hub 
operations could be broken down into two HOCs 
according to these seasonal periods. 
 
With regard to the large infrastructures, it may 
make sense to orient oneself to the company 
boundaries. If a port comprises two terminals for 
different cargo groups, both operated by the same 
company, they can be considered as follows: 
▸ two hubs with one HOC each, 
▸ one hub with two HOCs, if all hub operations can 
be completely assigned to only one HOC, 
▸ one hub with one HOC for which two emission 
intensity values are calculated by means of 
allocation (see Section 4.2.2). 
 
If the terminals in the port are operated by two 
different companies, it is common to consider 
them as two separate hubs, each with one HOC, 
due to the limited availability of data or the 
sensitivity of the data to external parties. 
 
In order to be able to establish relevant HOCs, 
Annex H of ISO 14083 lists examples of 
relevant HOC characteristics. 
 
For example, hubs can be grouped into one HOC 
due to different processes (1) such as sole or 
combined freight transhipment or passenger 
transfer, or (2) combined freight transhipment 
and storage. In addition, the characteristics can 
be further specified  
with regard to the inbound and outbound modes of 
transport (e.g. road/rail, road/water), size of the 
hubs (e.g. main and regional stations), age or level of 
technology of the site (e.g. non-/electrified 
processes, automated/manual processes). In 
addition to the processes, the ISO also lists the 
freight type as a HOC characteristic. The freight type 
is usually accompanied by different equipment and 
processes, making it a quick and universal 
differentiation criterion. And finally, it makes sense 
to distinguish between different temperature 
requirements (listed in ISO as "condition") of the 
goods. The processes can be carried out at ambient 
temperature (e.g. above +8 °C) or with temperature 
control, the latter including both heated (e.g. for 
liquid goods) and refrigerated (e.g. sensitive (0 °C to 
+2 °C), pharmaceutical products (+2 °C to +8 °C), 
frozen (below 0 °C or in the case of foodstuffs below 
-18 °C)). 
 
Based on this, hub operation categories can be 
structured with a sensible combination of 
characteristics influencing GHG emissions. 
4.2 Calculating the GHG emission intensities 
 
In principle, the calculation of the GHG emission 
intensities of a TOC or HOC requires the GHG 
emissions and the associated transport or hub 
activity. 
 
The calculation of GHG emissions is usually based on 
information on the GHG activities, i.e. data on the use 
of fuels and electricity, leaks and refrigerant losses 
are required. 
 
 
Table 4 
HOC characteristics    
Processes  Freight type Condition 
freight transhipment only 
passenger transfer only 
combined passenger and 
freight transfer 
freight transhipment and 
storage 
average/mixed 
containerised/swap bodies 
palletised 
piece goods/break bulk 
dry bulk  
liquid bulk  
vehicle transport  
other 
ambient 
temperature-controlled 
Source: ISO 14083 Table H.1  

---

## Page 30

Getting started with calculation and data 
collection 
30 
 
 
 
 
The GHG emissions are then calculated as follows: 
 
𝐺𝐻𝐺 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛 = 
𝐺𝐻𝐺 𝑎𝑐𝑡𝑖𝑣𝑖𝑡𝑦 × 𝐺𝐻𝐺 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑓𝑎𝑐𝑡𝑜𝑟 
 
This is established item by item for each GHG activity of 
the TOC or HOC. By summing up the calculated GHG 
emissions afterwards, the total GHG emissions of the 
TOCs or HOCs can be derived. 
 
A GHG emission intensity is then derived from the 
GHG emissions: 
 
𝐺𝐻𝐺 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛 𝑖𝑛𝑡𝑒𝑛𝑠𝑖𝑡𝑦 = 
 
𝐺𝐻𝐺 𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠
𝑡𝑟𝑎𝑛𝑠𝑝𝑜𝑟𝑡 𝑜𝑟 ℎ𝑢𝑏 𝑎𝑐𝑡𝑖𝑣𝑖𝑡𝑦 
 
In steps 3 and 4, the GHG emissions and GHG emission 
intensities are initially calculated only for the TOC and 
HOC levels, respectively. 
 
4.2.1 GHG emission factors 
In order to convert energy consumption (or 
fuel/electricity consumption) and refrigerant leakage 
into GHG emissions, reliable GHG emission factors of 
the various energy carriers and the refrigerants used 
are required. For energy carriers, these comprise of 
GHG emissions from operation and GHG emissions 
from energy provision. In the case of refrigerants, 
GHG emission factors refer only to GHG emissions 
from operation (i.e. leakage), i.e. excluding emissions 
from provision. 
 
A central requirement in ISO 14083 is to list the GHG 
emission factors used by the various energy carriers 
and to specify their source. In addition, the fuel type, 
lower heating value, density (for all liquid fuels) and 
(if used) biofuel blend (in % energy content) must be 
specified in each case. It is important that GHG 
emissions from operation do not only relate to 
(fossil) carbon dioxide emissions, but must also 
include GHG emissions of other gases with climate 
impact (nitrous oxide, methane) that can be produced 
during operation. 
 
 
 
In the case of biofuels, the approach in ISO 14083 is 
based on the EU Directive for Renewable Energy 
(European Parliament 2018). Accordingly, the 
cultivation and extraction of raw materials, 
GHG emissions from direct land use change, 
processing, transport and distribution are included 
in the GHG emissions of energy provision. The 
atmospheric CO2 bound during the cultivation of 
biomass is not accounted for, so the CO2 emissions 
generated during combustion are not taken into 
account, as both offset each other. However, other 
GHG emissions (e.g. from nitrous oxide or methane) 
also occur in the combustion of biofuels and must be 
taken into account. 
 
ISO 14083 also contains specifications on the 
methodology for deriving GHG emission factors for 
fuels and electricity, which must cover the entire life 
cycle of energy supply. In case of electricity, ISO 
14083 prescribes the use of location-based grid mixes. 
The GHG emission factors for electricity should refer 
to location-based consumption mixes; in contrast to 
the production mixes, they therefore also include net 
electricity imports from neighbouring countries. For 
regions or countries with low net electricity imports, 
the production mix and consumption mix are very 
similar in terms of production mix and consumption 
mix. 


---

## Page 31

31 
Getting started with calculation and data 
collection 
 
 
 
 
In the case of high electricity imports, the GHG 
emission factors of the consumption mixes can be 
either lower (if electricity is imported from countries 
with lower GHG emissions) or higher (if electricity is 
imported from countries with high GHG emissions) 
than those of the production mixes. In addition (not 
alternatively), GHG results that have been calculated 
using a market-based approach6 may also be reported. 
Possible sources and values for ISO 14083-compliant 
GHG emission factors of various fuels, energy carriers 
and refrigerants are contained in Annex A.5. 
 
Example 1: Calculating GHG emissions and  GHG emission 
intensities at a passenger station  
The HOC under consideration is a single station, at 
which annually 114,489,327 passengers start or 
finish their journey or have to change trains. The 
operator of the station measured the following 
consumption during this period: electricity 
(2,121,094 kWh), natural gas consumption 
(121,495 kWh) and district heating (703,125 kWh). 
 
The emission factors relevant to this calculation 
are listed in Annex A.3. The factor 3.6 MJ/kWh is 
used to convert the megajoule figures into kilowatt 
hours. 
 
GHG emissions of the HOC for operations 
 
▸ 121,495 kWh x 198.26 g CO2e/kWh = 24,088 kg 
CO2e GHG emissions of the HOC for energy provision 
▸ 2,121,094 kWh x 493.96 g CO2e/kWh + 121,495 kWh  
x 64.77 g CO2e/kWh + 703,125 kWh x 382.02 g CO2e/kWh  
= 1,324,218 kg CO2e 
 
GHG emission intensity of the HOC 
 
▸ Operation: 24,088 kg CO2e / 114,489,327 pax 
= 0.21 g CO2e/pax 
▸ Energy provision: 1,324,218 kg CO2e /  
114,489,327 pax = 11.57 g CO2e/pax 
▸ Total: 0.21 g CO2e/pax + 11.57 g CO2e/pax =  
11.78 g CO2e/pax 
 
4.2.2 Partitioning emissions by allocation  
Whenever a (transport or hub) process fulfils more than 
one function and these different functions are 
inextricably linked, the GHG activities or GHG emissions 
must be partitioned between the different freight or 
passenger groups.  
 
 
 
6 In the market-based method, the reporting organisation uses the GHG emissions of the electricity they purchase based on the values submitted by the 
electricity producer/seller. Various contractual instruments such as electricity purchase contracts, guarantees of origin, certificates for renewable 
electricity and energy certificates can be used. Further specifications for the calculation of market-based mixes can be found in ISO 14083 Annex J.3. 
 
 
 
Excursus: What should be considered for self-
generated electricity at hubs? 
 
The GHG emissions of a hub are calculated on the basis 
of the energy carriers or refrigerants used in the hub, 
regardless of what they are used for. At some hubs, 
electricity may partly be generated from energy 
carriers such as diesel. While the respective location-
based grid mix must be used for the electricity 
purchased by the hub, diesel consumption is used as 
the basis for calculation in cases a diesel-powered 
emergency power generator is in use, for example 
(this happens in some countries due to the unstable 
grid power supply). Even though ISO 14083 does not 
specify any requirements in this regard, the authors 
believe that this concept can also be transferred to 
renewable electricity generated within a hub, 
provided that the construction, operation and disposal 
of a corresponding plant infrastructure are taken into 
account. However, it is important that the electricity 
generated in this way is used exclusively internally 
(i.e. for the hub processes) and not made available to 
others (i.e. fed into the public power grid or sold 
elsewhere). Otherwise, the same applies to hubs: the 
location-based mix must always be used – but a 
parallel calculation with a market-based mix is 
allowed and can be reported additionally. 
 

---

## Page 32

Getting started with calculation and data 
collection 
32 
 
 
 
Table 5 
 
Passenger-equivalent values of Ro-Pax ferries and trains 
Passenger transport Passenger equivalent Freight transport  Passenger equivalent 
Passenger (including 
luggage) 
1.0 Light Commercial Vehicle 
N1-I/III 
1.3 
Passenger car 1.3 Light Commercial Vehicle 
N1-III 
3.5 
Bus 10.0 Solo truck, rigid truck 10 
Caravan, small  1.1 Articulated truck 18 
Caravan, medium  2.3 Unaccompanied trailer 14 
Mobile home/ caravan, 
large 
3.5   
Motorcycle 0.3   
 
Note: The information on the vehicles does not yet include the 
passengers (e.g. on the bus), these must be taken into account 
additionally. 
Note: Deviations from the standard values given here are possible, but 
must be justified. 
Source: based on ISO 14083 Table G.5 
 
This process is called "allocation". It must always be 
carried out if the primary data of the respective 
process cannot be recorded separately for the freight 
or passenger groups, for example when the same 
means of transport transports passengers and freight 
at the same time, as in air transport or ferries. ISO 
14083 stipulates that the allocation between freight 
and passengers must be based on the real mass. This 
also includes the baggage carried by the passengers 
and the outer packaging (but without additional 
cargo packaging such as pallets or the like, see 
Section 3.2.1). Since the exact masses are often not 
known, it is also possible to work with standard 
values. For example, when freight and passengers are 
transported together in air traffic, 100 kg per 
passenger including baggage can be applied in order 
to standardise different measured variables. An 
alternative to mass allocation can be the use of 
passenger equivalents, with the mode-specific 
annexes to ISO suggesting standard values for the 
passenger equivalents of the cargo that can be used. 
In the case of ferry transports, where passenger cars 
are also transported, this is even the recommended 
procedure. 
The following standard passenger equivalent values 
shown in Table 5 can be used for Ro -Pax ferries 7 and 
trains. 
 
Example 2: Allocation between cargo and passengers  
In this example, we are looking at a car train that 
transports vehicles as well as people. Since the energy 
consumption of the train is used to transport 
passengers and cars alike, the GHG activities and the 
GHG emissions of the train must be partitioned 
between the two functions. 
 
The car train under consideration here consists of 5 
wagons each for passenger transport (on average 
there are 60 seats in each wagon) and 5 wagons with 
car parking spaces (double-decker wagons with space 
for a total of 10 cars). On average, 6 vehicles are 
loaded on each car wagon, whereas it is generally 
assumed that the train transports only cars. The 
passenger wagons have an average occupancy rate of 
50%. On average, the car train transports 30 cars and 
150 passengers. Now the passenger cars can be 
converted into passengers by using the passenger 
equivalents (see Table 5) of 1.3. Since each passenger 
transported corresponds to one passenger 
equivalent, the entire car train carries 189 passenger 
equivalents; of these 150 passenger equivalents are 
attributable 
 
 
7 Ro-Pax ferries transport both freight and passengers at the same time. 
 
 

---

## Page 33

33 
Getting started with calculation and data 
collection 
 
 
 
to passenger transport and 39 passenger equivalents 
to passenger car transport. The ratio of the passenger 
equivalents of the passenger transport to the total 
passenger equivalents then results in the allocation 
key. In this case, 21% of the train's total GHG 
emissions would be attributed to passenger cars and 
79% to passengers. 
 
Example 3: Calculation of a collection/delivery round 
Collection and delivery rounds are trips where goods 
are collected or delivered at various locations along a 
vehicle's route. Since it is not reasonable to partition 
the GHG emissions of a collection and delivery round 
to the freight based on the actual distances travelled (as 
freight delivered early in the tour would fare much better 
than freight remaining in the vehicle for a long time), an 
allocation is usually applied here as well. In this example, the 
SFD between the respective pick-up and delivery locations of 
a shipment is used for calculation. Alternatively, the use of the 
GCD would also be possible.  
 
If the respective freight masses as well as the pick-up and 
delivery locations are known, the allocation can be made on 
the basis of the transport activity data of the individual 
shipments (or the sum of the total transport activities of the 
tour). 
 
Figure 6 
 
Collection and delivery round 
 
Source: own illustration, ifeu/Fraunhofer IML 


---

## Page 34

Getting started with calculation and data 
collection 
34 
 
 
 
 
Table 6 
 
Allocation of a collection and delivery round  
 
Actual distance 
travelled 
(cumulative) (km) 
Distance hub – 
destination (SFD) 
(km) 
Weight of 
shipment (kg) 
Tonne kilometres 
(SFD) (tkm) (1) 
Allocation key 
(2) 
1 8 7 4 0.0280 7.7 % 
2 10 7.2 1 0.0072 2.0 % 
3 14 9 0.25 0.0023 0.5 % 
4 14.5 8.9 2 0.0178 4.9 % 
... ... ... ... ... ... 
14 40 7 0.5 0.0035 1.0 % 
Hub 44 - - -  
Tour 44 - 45.3 0.3632 100.0 % 
 
Note: (1) Tonne-kilometres = SFD x shipment weight; 
(2) Allocation key = tonne-kilometres of the stop / tonne-kilometres 
of the tour 
Source: own calculation, ifeu/Fraunhofer IML 
 
An example calculation of the allocation key per 
shipment is shown in Table 6. 
 
It is important to note that if measured primary data 
for the fuel consumption of the entire collection and 
delivery round are available, the distance actually 
driven by the vehicle is not required for the 
calculation of GHG emissions. Only if the fuel 
consumption of the tour is calculated using GHG 
emission intensities, that has been determined on 
the basis of actual distances, the actual distances 
must also be known. 
 
If the freight masses are not known, an allocation can 
also be made on the basis of the number of shipments; 
however, this (trivial) calculation method is not 
outlined here. 
 
Example 4: Allocation of GHG emissions in 
temperature -controlled maritime transport  
A container ship sails from Hamburg to Singapore 
(approx. 16,000 km) and has loaded 6,000 TEU. Of 
these, 950 TEU are reefer containers. This sea freight 
represents the transport operation category (TOC) 
(characteristics according to ISO Table G.1: 
"Container, mixed ambient and temperature-
controlled, scheduled"). The GHG emission intensities 
for ambient and reefer containers for this TOC are to 
be determined. As GHG activities, the propulsion and 
cooling of the reefer containers are considered, both 
consuming maritime fuel oil (MFO). 
 
 
At best, the consumption for cooling is measured 
separately. In this example, however, it is not known 
how much of the MFO consumption is caused by 
cooling. An allocation key is therefore required for the 
allocation of partial consumption to cooling. For this 
purpose, research results from the Universidad de los 
Andes on container terminals are used, according to 
which reefer containers cause 17% more GHG 
emissions than ambient containers (Dobers et al. 
2023b). 
 
If it is assumed that 950 TEU of the total containers 
transported (6,000 TEU) are cooled, this results in 
6,162 TEU equivalents. This key can be used to divide 
the total MFO consumption of 88,090,000 MJ, for 
example: For this purpose, a consumption per TEU 
equivalent is first calculated (14,298 MJ/TEUeq), and 
then this value is multiplied by the respective TEU 
equivalents of the ambient and reefer containers. As a 
result, 72,199,059 MJ are allocated to the transport of 
ambient containers and 15,890,941 MJ to the 
transport of reefer containers. GHG emissions are 
then calculated, as explained elsewhere in the guide. 

---

## Page 35

35 
Getting started with calculation and data 
collection 
 
 
 
 
▸ 950 TEU x 1.17 + 5,050 TEU x 1 = 6,162 TEUeq 
 
▸ 88,090,000 MJ / 6,162 TEUeq = 14,297 MJ/TEUeq 
 
▸ 14,297 MJ/TEUeq x 5,050 TEUeq (ambient) = 
72.199.059 MJ (ambient) 
 
▸ 14,297 MJ/TEUeq x 1,112 TEUeq (reefer) = 
15,890,941 MJ (reefer) 
 
 
Example 5: Hub calculation with allocation  
One company operates two transhipment hubs 
(A) and (B) in Germany and, at the request of its 
customers, requires the GHG emission intensities for 
the handling of goods. Both hubs handle both ambient 
and chilled goods, both hubs have comparable 
equipment and comparable process flows and are 
therefore combined into one hub operation category 
(HOC). In addition to the ambient goods, a specific 
group – the group of chilled goods – is defined for this 
HOC. The GHG emission intensities are calculated for 
both product groups. This is therefore an example of 
the case of a HOC of freight with multi-temperature 
conditions (see ISO 14083 section 9.5.3). 
 
The table below lists all primary data on energy 
consumption and refrigerant leakage. Refrigerant 
leaks were measured by the annual refill quantity. In 
addition, there are separate metering points on the 
cooling systems (CS), so that 40,300 kWh (Hub A) or 
44,020 kWh (Hub B) can be allocated to cooling. 
However, the amount of electricity required to light 
indoor areas in which only cooled goods are handled 
(e.g. cold warehouse) and those in which all goods 
are handled (e.g. goods receipt, dispatch) is 
unknown. In order to estimate the respective 
electricity consumption, it is first assumed that 32% 
of site consumption (130,000 kWh (Hub A) and 
142,000 kWh (Hub B)) can be attributed to lighting 
(Dobers et al. 2023a), i.e. 41,600 kWh at Hub 1 and 
45,440 kWh at Hub 2. The proportion of the cooled 
area can serve as an allocation key: the cooled area 
accounts for one fifth of the area of the respective 
hubs, resulting in an electricity consumption of 8,320 
kWh (Hub A) or 9,088 kWh (Hub B) for the lighting of 
the cooled surfaces (L). (Note: This is a simplified 
example.  
in reality there are probably also illuminated areas 
with only ambient goods.) 
 
The natural gas or district heating is used to heat the 
hubs and is therefore only allocated to the ambient 
goods. All other GHG activities (i.e. residual electricity 
consumption, diesel and LNG) are assigned to all 
goods. 
 
In the first step of the calculation, the emissions of the 
respective specific group and the emissions affecting 
all goods/groups are calculated. To do this, the 
respective quantities of energy carriers or refrigerants 
are multiplied by the relevant GHG emission factor. 
 
The conversion and GHG emission factors relevant to 
this calculation are listed in Annexes A.1, A.3 and A.4. 
 
The GHG emissions of the HOCs of the respective groups are 
now calculated as follows: 
 
Group "cooled" 
 
▸ for operation: 9 kg x 2,255.5 kg CO2e/kg = 
20,300 kg CO2e 
 
▸ for energy provision: 101,728 kWh x  
493.96 g CO2e/kWh = 50,250 kg CO2e 
 
Group "ambient" 
 
▸ for operation: 52,000 kWh x 198.26 g CO2e/kWh = 
10,310 kg CO2e 
 
▸ for energy provision: 52,000 kWh x  
64.77 g CO2e/kWh + 37,000 kWh x 
382.02 g CO2e/kWh = 17,503 kg CO2e 
 
Group “all” 
 
▸ for operation: 11,110 l x 2,639 g CO2e/l + 5,500 kg x 
2,467 g CO2e/kg = 42,888 kg CO2e 
 
▸ for energy provision: 170,272 kWh x 493.96 g 
CO2e/kWh + 11,110 l x 801 g CO2e/l + 
5,500 kg x 1,050 g CO2e/kg = 98,782 kg CO2e 

---

## Page 36

Getting started with calculation and data 
collection 
36 
 
 
 
 
 
Table 7 
Primary data on the freight transhipment in Hub 1 and Hub 2  
GHG activity Hub Specific groups 
– chilled 
Specific groups 
– ambient 
All (chilled 
and ambient) HOC 
Electricity [kWh/a] A CS: 40,300 
L: 8,320 
CS: 44,020 
L: 9,088 
 
101,728 
 
81,380 
272,000 
B 
88,892 
  
Natural gas [kWh/a] A  52,000  52,000 
District heating [kWh/a] B  37,000  37,000 
Diesel [l/a] A   7,654 
11,000 B 3,456 
LNG [kg/a] A 
B   3,200 
2,300 5,000 
Refrigerant R-410A [kg/a] A 5   9 B 4 
Hub activity [tonnes/a] A 4,000 70,000  143,000 B 2,000 67,000 
 
 
In the next step, the emission intensities for cooled 
and ambient goods are calculated in the HOC. 
 
GHG emission intensity of the HOC of 
cooled goods 
 
▸ for operation: 42,888 kg CO2e / 143,000 t + 
20,300 kg CO2e / 6,000 t = 3.68 kg CO2e/t 
 
▸ for energy provision: 98,782 kg CO2e / 
143,000 t + 50,250 kg CO2e / 6,000 t = 
9.07 kg CO2e/t 
 
GHG emission intensity of the HOC of 
ambient goods 
 
▸ for operation: 42,888 kg CO2e / 143,000 t + 
10,310 kg CO2e / 137,000 t = 0.38 kg CO2e/t 
 
▸ for energy provision: 98,782 kg CO2e / 
143,000 t + 17,503 kg CO2e / 137,000 t = 
0.82 kg CO2e/t 
The calculated GHG emission intensities (cooled: 
12.75 kg CO2e/t or ambient 1.19 kg CO2e/t) can be 
multiplied by the customer-specific quantity of 
cooled or ambient goods, so that the emissions for 
the customer's goods handling can be reported. 
 
Allocation can be quite a complex task, depending on 
the number of hubs grouped together in a HOC and 
the number of different types of energy carriers and 
refrigerants, as well as specific groups according to 
which a distinction is to be made. It is therefore 
useful to check whether all emissions are actually 
reflected in the emission intensity values. For this 
purpose, all GHG emissions are summed up on the 
one hand and the emission intensities are multiplied 
by the respective HOC activities of the groups on the 
other. Both results should result in the same amount 
of total GHG emissions. 
 
4.2.3 Data collection and level of detail 
Data collection must be carried out both for 
determining transport and hub activities and for 
identifying GHG activities. 

---

## Page 37

37 
Getting started with calculation and data 
collection 
 
 
 
 
As described in Section 2.2, the use of primary data 
(measured data) is preferable to the use of secondary 
data (modelled data or default data). 
 
The use of the various data types depends primarily 
on the availability of primary data (or the effort 
required to collect such primary data itself). However, 
under no circumstances should the decision on the 
chosen data type be made on the basis of a lower GHG 
emission result (see ISO 14083 Section 7.2.2). 
 
Measured data / primary data  
Measured data or primary data will be used primarily 
in the quantification of GHG activities (e.g. energy 
consumption data and refrigerant losses). However, 
other values can also be determined on the basis of 
primary data, such as the transport and hub activity 
(e.g. based on measured freight amounts/passenger 
counts and distances). In addition, GHG emission 
factors of the various energy carriers (including 
electricity) or of refrigerants and GHG emissions from 
operation can also be based on measured data (e.g. 
measured methane or nitrous oxide emissions from 
fuel combustion or slippage). 
 
A central field of application for measured data is the 
(usually relatively easily obtained) energy 
consumption of transport and hub operations. The 
collection can be carried out, for example, by: 
 
▸ Use of measurement interfaces (e.g. reading out a 
vehicle diagnostic system or electricity meters at 
hubs or selected equipment (e.g. cooling system) 
 
▸ Evaluation of energy bills (e.g. energy carriers or 
heat quantities supplied to hubs or refuelling 
protocols or electricity quantities for vehicles) 
 
It is important here that a distinction is made 
between the energy carriers used (different types of 
fuel / electricity) so that GHG emissions can then be 
calculated from these consumption data using 
suitable GHG emission factors. Refrigerant losses can 
be determined and documented on the basis of the 
measured refill quantities per refrigerant type. 
The measured data does not necessarily have to be 
collected by the reporting organisation itself, it can 
also be fed by data provided from a subcontractor or 
supplier. 
 
The quality of primary data is determined primarily 
by the application of the correct measurement 
methods and an (independent) verification of the 
data obtained. 
 
Modelled data / secondary data  
In the case of the use of secondary data, modelled 
data is particularly noteworthy, as it often allows for 
a high degree of detail. This means that modelled data 
can deliver much more specific results than the use of 
default values. Many of the models used are originally 
based on measured data that were determined for 
representative vehicles and operational situations 
and later generalised to cover other areas. 
 
Modelled data can also cover the various data 
requirements. Among other things, the transport 
operations can be modelled on the basis of routing 
that is as realistic as possible, taking into account the 
transport network and other local and technical 
conditions (e.g. access restrictions for vehicles above 
a certain weight class), and this, with the help of 
information on freight/passengers, can be used to 
determine the relevant transport activity. 
 
By modelling the energy consumption of the various 
energy carriers (supplemented by statistical data on 
biofuel shares, if required) and the use of GHG 
emission factors, GHG emissions can be determined 
for the individual transport and hub operations. GHG 
emissions from operations can also be modelled, 
taking into account the specific circumstances and by 
using suitable model data (e.g. emission data from 
the Handbook for Emission Factors (INFRAS 2023)). 
 
It is important that the model used and its data bases 
are documented as well as possible in order to enable 
sufficient transparency and verifiability of the 
calculation results. It is advantageous if the model 

---

## Page 38

Getting started with calculation and data 
collection 
38 
 
 
 
 
includes all relevant characteristics, such as specific 
vehicle characteristics (vehicle type, configuration, 
size, emission class, age), the fuel types used, the 
proportion of empty runs and load factor, as well as 
the local conditions (topography and traffic 
situation). 
 
Default values / secondary data  
Default values are always used when neither primary 
data nor modelled data is available. They are often 
used as a supplement to the other two data types to 
fill data gaps, and are also suitable for evaluating 
processes with low effort, 
if those are less relevant to the overall result of the 
GHG emission calculation. 
 
Default values can also be of different data quality. 
Both rough estimates for processes for which no 
measured data is currently available as well as default 
values that have been determined on the basis of a 
(large) amount of different measured data can be 
used. The better the default values match the TOCs 
under consideration and their essential 
characteristics, the better they are suitable for the 
specific application. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Table 8 
Origin of consumption data     
Data cases for GHG activities  Origin Examples Use in GHG emission 
calculation 
(1) Consumption (total) Measurement 1,000 litres diesel 1:1 
(2) Consumption (subset)  Measurement 800 litres diesel Extrapolation, 
e.g. with transport/ 
hub activity, time 
(3) Activity-based consumption metric 
differentiated according to TOC characteristics:  
Measurement of 
a. same processes, same period *  
b. same processes, different time period**  
c. other processes***, same period of time  
d. other processes***, other time period**  
Calculated 
on the basis 
of measured 
values  
x litre diesel /tkm  
x kWh electricity /t  
x litre diesel /t 
Multiplication by 
transport or hub activity  
(4) Activity-based consumption metric 
differentiated according to TOC characteristics:  
Measurement of usually other processes*** and 
other time period** 
Calculated on the 
basis of measured 
values or by 
modelling  
x litre diesel /km  
x litre diesel /tkm 
Modelling, e.g. 
based on load 
factor and 
transport activity 
Continued next page 
 
Excursus: Differentiation between primary and secondary data 
The input data used is essential for any GHG emission calculation. As explained above, the 
respective data must be representative of the transport chain element under consideration 
and fit as well as possible geographically, in terms of time and technology , in order to obtain 
a meaningful result. The following explanations are not taken directly from ISO but have 
been prepared for this guide for illustrative purposes. They do not claim to be complete and 
can only serve as a guide in distinguishing between primary data and secondary data. 
 
Table 8 uses examples of consumption data (e.g. fuel consumption of a vehicle, electricity 
consumption in a hub) to illustrate the types of data that can exist and their origin and use. 
The following text explains how this consumption data could be classif ied. 

---

## Page 39

39 
Getting started with calculation and data 
collection 
 
 
 
 
Table 8 (continued) 
Origin of consumption data     
Data cases for GHG activities  Origin Examples Use in GHG emission 
calculation 
(5) Activity-based GHG emission indicator  
differentiated according to TOC characteristics:  
Measurement of usually other processes*** and other 
time period** 
Calculated on the basis 
of measured values or 
by modelling  
x g CO2e/km  
x g CO2e/tkm 
Modelling, e.g. 
based on occupancy and 
transport activity  
(6) GHG emission intensity  
e.g. differentiated according to TOC characteristics  
Modelling of 
application scenarios  
**** 
x g CO2e/tkm  
x g CO2e/pkm 
Multiplication by transport or 
hub activity 
*  i.e. direct measurement and comparable to (1) or (2) 
**  e.g. previous year, average value over several years 
***  e.g. in your own company or in another company 
****  e.g. inner-city transport with a bus-type A, with a truck-type B 
 
 
 
Typical examples of primary data are thus case (1) the measured total consumption of a transport or 
hub operation or case (2) the measured and subsequently extrapolated partial consumption of a 
transport or hub operation in a selected observation period of one year (e.g. consumption is on ly 
available for 11 out of 12 months). 
 
A company can also decide to measure its own fuel consumption and the associated transport 
performance, for example, and to map it using its own key figures by calculating activity -based 
consumption figures, e.g. in litres of diesel per tonne-kilometre (tkm). Depending on the measurement 
period or vehicle (transport operation) to which the key figures refer, they are direct measured data of 
the transport operation under consideration, i.e. case (1), (2) and (3a) (see Table 8), or they refer, for 
example, to another measurement period, possibly to other vehicles as in case (3c) or (3d). This is the 
case, for example, if a company uses indicators that have been calculated with measurement data from 
the previous year or from the entire fleet. For the GHG emission calculation, the company must decide 
whether the key figures are representative for the transport chain element under consideration. 
 
Two typical examples of modelled data are cases (4) and (5) when activity-based consumption or GHG 
emission indicators taken from a general database are used in the GHG emission calculation. These key 
figures are given, for example, in litres of diesel per vehicle kilometre (possibly differentiated between 
empty and fully loaded vehicles) or already converted into grams of GHG emissions per vehicle 
kilometre. The data used in cases (4) and (5) are based on measurements. But they are measurements 
of other transport operations at different time periods than those of the transport chain(s) under 
consideration, or they come from measurements in test rigs for engines in which transport processes 
are reproduced. By means of a vehicle load factor and transport activity suitable for the application, the 
total consumption or GHG emissions of the TOCs can be model led. This can be done in a very 
differentiated way depending on the level of detail of the indicator. 
 
ISO 14083 does not clearly define where exactly consumption data is to be classified as secondary data 
or as primary data, such as the sub-cases in case (3). For example, "direct measurement" (see ISO 14083 
Section 3.3.3) can mean very narrowly that the data has to refer to the same transport operations in the 
same period as the TCE under consideration (case (3a)) in order to be considered primary data ; 
however, data from the same transport operations (e.g. the same  vehicle, same tour) of another period 
(case (3b)) not. 

---

## Page 40

Getting started with calculation and data 
collection 
40 
 
 
 
 
 
 
4.2.4 Excursus: Refrigerant leakage in transport and 
transhipment 
The task of temperature-controlled transports is to 
maintain a specified temperature during transport (see 
ISO 14083 Annex I.1). 
For this purpose, air conditioning systems and 
temperature-control units are used in both passenger 
transport and freight transport. These temperature-
control units are filled with refrigerants but may lose a 
proportion of the refrigerants during operation. Since 
most refrigerants are gases that have a strong impact on 
the climate, they must be included in the GHG emission 
assessment of transport chains. 
 
The consumption of refrigerants can usually be 
measured on the basis of the amount refilled. Refilling 
is usually carried out during the annual inspection at 
hubs of the companies or external partners. When 
refrigerants are refilled in vehicles or loading units (e.g. 
reefer containers), the corresponding amount must be 
added to the GHG emission calculation of the transport 
TCE and not in the TCE of the hub where the refilling 
takes place. 
 
The emission factors to be used for refrigerants should 
reflect GHG emissions from operation and must not 
include production and supply processes (see ISO 14083 
Section 5.2.4). Corresponding GHG emission factors of 
refrigerants are compiled in the annex. 
 
Refrigerant leakage in transport  
If no primary data can be collected for the refill quantity 
of refrigerants, ISO 14083 provides an approach to 
quantity estimation in Annex I. For trucks for which the 
load factor is not known, it specifies a value range of 3 to 
8 kg of refrigerant and recommends using the average 
value of 5.5 kg for mobile freight units with temperature-
control. 
The annual loss rate can range from 15% to 50%. At 
this point, however, the use of the highest value for the 
loss rate (i.e. 50%) is recommended to use in order to 
follow the principle of a conservative calculation. 
Freight forwarders report an annual refill rate of 
approx. 1 kg per temperature-control unit as part of 
inspection for mobile freight units with temperature-
control (Wagner vom Berg et al. 2023), which is rather 
in the lower range of the ISO recommendation and 
equals a refill quantity of 32.5%. 
 
In addition to the amount lost, the type of refrigerant 
used in each case is also essential for the GHG emission 
calculation due to the very different emission factors 
(see Annex A.4). According to the NOW-study on 
temperature-control units in road freight transport 
published in 2023 (Wagner vom Berg et al. 2023), the 
refrigerants R-404A, R-410A and R-452a are currently 
frequently used. In addition, the newer refrigerants R-
449A and R-454C are mentioned. It is expected that R-
404A will successively be replaced by R-452a, as it is 
less harmful to the climate and R-404A has also been 
banned since 2020 according to the F-Gas Regulation 
(Regulation (EU) No. 517/2014) is prohibited in new 
vehicles (Wagner vom Berg et al. 2023). If it is not 
known which refrigerant is used in the temperature-
controlled transports, a conservative approach is 
recommended, i.e. R-404A should be used for older 
vehicles and R-452a for newer vehicles. 
 
Example 8: Loss of refrigerant s during transport  
In Case example A, transports in a truck with a 
temperature-control unit are also conceivable as an 
alternative. For this the leakage of the refrigerant R-
452a used is unknown and should be estimated by 
means of the annual refill quantity.  
This would even also be the case if the measured data were independent of the actual measurement 
period in a very constant process and thus constant consumption.  
 
Default data are, for example, GHG emission intensity values, which are included in the GHG emission 
calculation by multiplying it by the relevant transport or hub activity, see in particular case (6). These 
indicators may have been worked out on the basis of measurements, but apart from matching TOC 
characteristics, they have no direct relation to the transport or hub operation under consideration. 

---

## Page 41

41 
Getting started with calculation and data 
collection 
 
 
 
 
To this end the freight forwarder assumes the 
average refill rate (32.5%) of a medium-sized 
refrigeration unit (5.5 kg) according to ISO 14083 
Annex I for the truck, which in this example 
represents the TOC. 
 
▸ 5.5 kg R-452a x 32.5% = 1.7875 kg R-452a 
 
If the freight forwarder documents the refill quantity 
during the regular inspection of his trucks, he can use 
this primary data in the calculation instead of an 
estimate. However, it should be noted here that the 
inspection and refill cycles may not correspond to the 
reporting period of the TOC to be evaluated. For 
example, the transport performance is to be 
calculated in tonne-kilometres for the calendar year 
2023, but the inspection protocols cover the period 
from March to February of the following year. The 
assignment to the respective calendar year can be 
established by calculating a monthly average value of 
each fiscal year. 
 
▸ 04/2022 – 03/2023: 
1.700 kg refill/12 months =  
0.1417 kg/month 
 
▸ 04/2023 – 03/2024: 
1.805 kg refill/12 months =  
0.1504 kg/month 
 
▸ 01/2023 – 12/2023: 
0.1417 kg/month x 3 months + 
0.1504 kg/month x 9 months = 1.7788 kg 
 
While the data from the estimate in accordance with 
Annex I of the ISO are to be regarded as secondary 
data (default values), the data from the freight 
forwarder's measurements represent primary data. 
Although the freight forwarder could not use the data 
from his measurement 1:1, he was able to calculate 
the refill quantity based on direct measurements. 
 
The GHG emissions associated with the loss of 
refrigerant are calculated by multiplying the 
refill quantity (regardless of whether 
these are secondary or primary data) with the 
GHG emission factor of the refrigerant (see Annex A.4), 
shown below on the basis of the primary data. 
 
▸ 1.7788 kg R-452a/a x 2,292 kg CO2e/kg R-452a = 
4,076 kg CO2e/a 
 
In order to be able to assign the absolute annual 
leakage to the transport chain element or the TOC, the 
GHG emissions must still be linked to the annual 
transport performance of the truck (or TOC). In this 
example, it is assumed that that the annual TOC activity 
of the 40 t tractor-trailer is 1,800,000 tkm. 
 
▸ 4,076 kg CO2e/a / 1,800,000 tkm/a = 
2.26 g CO2e/tkm 
 
This GHG emission intensity due to refrigerant 
leakage must be added to the GHG emission 
intensity caused by fuel consumption of the TOC. 
 
Refrigerant leakage at hubs 
According to a survey conducted in the period 
2021 to 2023, 66% of the approximately 850 
participating site operators confirmed that 
refrigerants are refilled annually at logistics hubs: 
The most common refrigerants used by operators 
were R-410A and 404A (19% each), R-717 (15%), 
R-407C (8%), R-134a (6%) and R-448a and R-744 
(5% each). According to the study, especially R-
717 (ammonia), R -744 (carbon dioxide), R -404A, 
R-410A and R-1234yf are used in hubs with more 
than 40,000 m² (Dobers and Jarmer 2023). 
 
In the absence of primary data on refrigerant 
leakage at the hub, an approximation of an average 
refill of 0.5 g of R-404A per tonne of ambient cargo 
and 1.2 g of R-404A per tonne of temperature-
controlled cargo can be assumed.8
 
 
 
8 Note: Refill quantities reported are based on a small sample of logistics hubs that provide complete data sets on refrigerant type, refill quantity, and 
throughput at the site (source: GILA project). Further research is needed here to derive representative key figures. In order to take a conservative 
approach, the refrigerant with the highest emission factor from the above list was chosen, i.e. R-404A. 
 
 

---

## Page 42

Getting started with calculation and data 
collection 
42 
 
 
 
Example 9: Refrigerant leakage at the logistics hub  
The refrigerant R-410A is used in a deep-freeze 
warehouse, and 15 kg of this refrigerant is refilled 
during the period under review. In addition, the site 
consumes 2,000,000 kWh of electricity in the same 
period. The GHG emissions of the hub for operation 
(i.e. from refrigerant losses) are thus calculated as 
follows: 
 
▸ 15 kg x 2,255.5 kg CO2e/kg = 33,833 kg CO2e. 
The calculated amount of GHG emissions due to 
refrigerant losses accounts for a share of 3.3% 
compared to that of electricity consumption 
(2,000,000 kWh x 493.96 g CO2e/kWh =  
987,926 kg CO2e). 
4.3 Case examples Part 2 
In Section 3.3, the first two steps were carried out for 
the case examples and the transport chain, the 
transport chain elements and the associated transport 
and hub operations were determined. Now follow 
steps 3 and 4. 
 
 
Case example A: Transport services in freight transport (continued from page 25)  
 
For the further greenhouse gas calculation, the company wants to determine the GHG emission 
intensities. 
 
Step 3: Assign the TO/HO to TOCs or HOCs  
In step 3, the characteristics of the various transport chain elements are examined in more detail and 
similar transport or hub operations are grouped into transport or hub operation categories in order to 
facilitate data collection. 
 
The company decides to combine TCE 1 and TCE 5 into one TOC A, as a modern diesel articulated 
truck is used in both cases. Enquiries with the transport companies carrying out the work show that 
vehicles with Euro 6 A-C emission standards are used in the pre-carriage and onward carriage. The 
load of the transported container is known to be 10 t. Since the standard container (TEU) has a 
capacity of about 20 t, this corresponds to an average load of 50%.  
 
TCE 3 is managed as a separate TOC B and refers to an electrically powered container train with a 
gross weight of 1,000 t. 
 
The two transport chain elements of the hub operations are also combined into HOC A, as in both 
cases the transhipment takes place at an intermodal terminal. 
 
The following figure visualises the transport chain elements and the assignment to the HOCs/TOCs.  

---

## Page 43

43 
Getting started with calculation and data 
collection 
 
 
 
 
 
Figure 7 
 
Illustration of steps 3 and 4: Assignment of TOC and TO to the transport chain to be evaluated  
Source: own illustration, ifeu/Fraunhofer IML 
 
 
For TOC A (road), TOC B (rail) and HOC A, the company wants to determine the GHG emission 
intensities in step 4. The various GHG activities are indicated separately from each other and a 
distinction is made between the energy carriers. Since the transported goods do not have to be cooled, 
there is no need to account for refrigerant losses. This means that GHG activities are limited to the use 
of energy carriers, namely diesel for the truck and electricity for the freight train. Thus, no allocation is 
to be carried out here. 
 
Since the company does not have primary data for HOC A, it decides to use default values (secondary 
data). It uses the default value of 10.7 kg CO2e/container transhipment from the GLEC Framework 
(Smart Freight Centre 2023). Together with a conversion factor of 10 tonnes per container, this 
results in a factor of 1.07 kg CO2e per tonne transhipped, which is used for the example. 
 
For both TOCs, the company uses modelled data. For TOC A, a 40-tonne diesel articulated truck of the 
Euro 6a-c emission standard with a load capacity of 10 tonnes is used. Since the company does not 
have any information on the complete round trip of the articulated trucks, it uses a default value of 
20% for the average share of empty runs. For TOC B, an electric freight train is used. For this a 
container train with an average load of 48% and a share of empty runs of 20% is used (EcoTransIT 
World 2023). 

---

## Page 44

Getting started with calculation and data 
collection 
44 
 
 
 
 
 
 
 
The calculation process is only shown here in a highly simplified form. As a result of the calculation 
with EcoTransIT World, the GHG emission intensity of TOC B (freight train) is  14 g CO2e/tkm (energy 
carrier: electricity). For TOC A, the GHG emission intensity is based on the actual distance and accounts 
for 143 g CO2e/tkm (total GHG emissions, of which 103 g CO 2e/tkm from operation). The energy 
carrier is diesel/biodiesel blend with 6.3% biodiesel. By means of the distance adjustment factor, this 
value must be converted into a GHG emission intensity related to the SFD. 
 
The company uses these GHG emission intensities to calculate the GHG emissions of the TOCs as 
follows: 
 
▸ GHG emissions TOC A: 143 g CO2e/tkm x (525 tkm + 1,050 tkm) = 225.2 kg CO2e  
(based on actual distance) 
 
▸ GHG emissions TOC B: 14 g CO2e/tkm x 5,000 tkm = 70.0 kg CO2e 
 
For the conversion to GHG emission intensity of the TOCs, the transport activity bas ed on the shortest 
feasible distance is now used: 
 
▸ GHG emission intensity TOC A: 225.2 kg CO2e / (500 tkm + 1,000 tkm) = 150 g CO2e/tkm  
(of which 108 g CO2e/tkm from operation) 
 
▸ GHG emission intensity TOC B: 70.0 kg CO2e / 5,000 tkm = 14 g CO2e/tkm 
(of which 0 g CO2e/tkm from operation) 
 
▸ GHG emission intensity HOC A: 1,070 g CO2e/t (of which 384 g CO2e/t from operation 
(own calculation based on (Dobers et al. 2023b)) 
 
The GHG emission factors used for the energy carriers (including electricity) are documented in Annex A.3. 
 
This example shows how important it is to specify the distance used in each case to understand the results.  
 
 
The bus company decides to combine the buses into TOCs based on their fuel type and size. These TOCs also 
roughly coincide with certain bus lines, as the buses usually run on the same lines. For example, electric 
buses tend to run on shorter, inner-city routes (TOC B), while diesel standard buses tend to run on less used 
routes (TOC A). However, partly different types of buses are also in use on one line. For example, one line is 
served by an articulated bus (TOC A) during the morning’s dense commuter traffic, while a standard bus 
(TOC C) is used at night on the same line. 

---

## Page 45

45 
Getting started with calculation and data 
collection 
 
 
 
 
 
 
Table 9 
 
Data for Case example B 
 Diesel 
consumption 
(MJ/km) 
Electricity 
consumption 
(MJ/km) 
Annual 
mileage per 
bus 
Capacity 
per bus 
Number of 
buses 
TOC A: 
Articulated diesel bus 
14.1 – 55,000 km 90 seats 14 
TOC B: 
Articulated electric bus 
– 7.5 50,000 km 90 seats 2 
TOC C: 
Standard diesel bus 
10.7 – 52,000 km 60 seats 3 
Note: Seats on the bus include both seating and standing. Source: own calculation, ifeu/Fraunhofer IML 
 
The company thus considers the following TOCs: 
 
▸ TOC A: 12 articulated diesel buses Euro 6 a-c + 2 articulated buses Euro 6 d-e (corresponds to TCEs 1 to 14) 
 
▸ TOC B: 2 articulated electric buses (equivalent to TCEs 15 and 16) 
 
▸ TOC C: 4 standard diesel buses Euro 6 a-c + 1 standard diesel bus Euro 5  
(corresponds to TCEs 17 to 21) 
 
Since the fuel consumption of buses with the same type of drive and the same size hardly differs between the 
different emission classes, the TOCs include buses with different emission standards. 
Euro levels. 
 
 
All the data on the buses available to the company are shown in Table 9.  
 
 
 
For all buses, the determined uniform average occupancy rate of 18% is used. 
 
Using the GHG emission factors for diesel or electricity (see Appendix A.3), the company can calculate the GHG 
emissions of the TOCs and their GHG emission intensities. 
 
In this case example, the total GHG emissions of a TOC can be calculated as follows:  
 
GHG emissions = consumption x number of vehicles x annual mileage x GHG emission factor 
 
This results in the following values per TOC and year: 
 
▸ TOC A: 1,018,387 kg CO2e (of which 766,508 kg CO2e from operation) 
 
▸ TOC B: 46,125 kg CO2e (of which 0 kg CO2e from operation) 

---

## Page 46

Getting started with calculation and data 
collection 
46 
 
 
 
 
 
▸ TOC C: 260,952 kg CO2e (of which 196,409 kg CO2e from operation) 
 
Subsequently, the transport activities of the TOCs per year are calculated: 
 
▸ TOC A: 14 vehicles x 55,000 km/a x 90 passengers x 0.18 = 12,474,000 pkm 
 
▸ TOC B: 2 vehicles x 50,000 km/a x 90 passengers x 0.18 = 1,620,000 pkm  
 
▸ TOC C: 5 vehicles x 52,000 km/a x 60 passengers x 0.18 = 2,808,000 pkm  
 
By dividing these GHG emissions by the associated transport activities of the respective TOCs, the GHG 
emission intensities of the TOCs are determined, which are as follows:  
 
▸ TOC A: 82 g CO2e/pkm (of which 61 g CO2e/pkm from operation) 
 
▸ TOC B: 28 g CCO2e/pkm (of which 0 g CO2e/pkm from operation) 
 
▸ TOC C: 93 g CO2e/pkm (of which 70 g CO2e/pkm from operation) 

---

## Page 47

47 
 
 
 
5 Calculation of GHG emissions of a transport chain 
5.1 From GHG emission intensity to GHG 
emissions of TCEs and TC 
In order to get from the GHG emission intensity of the 
different TOCs or HOCs to the GHG emissions of the 
TCEs, the transport or hub activity of each TCE is 
multiplied by the corresponding GHG emission 
intensity of the respective TOC or HOC. Care must be 
taken to ensure that – unless the base unit of tonnes or 
tonne-kilometres has been used – a uniform unit for 
transport or hub activity or uniform conversion factors 
(see Annex A.1) are used. 
 
GHG emissions of the TCE = 
GHG emission intensity TOC or HOC x 
transport or hub activity of the TCE 
 
By adding up all GHG emissions of the TCEs of a 
transport chain, the total GHG emissions of this 
transport chain are determined. These can then be 
converted back into a GHG emission intensity of the 
transport chain by dividing the GHG emissions of the 
transport chain by the sum of the transport activity of 
the transport chain. 
 
GHG emissions of TC = 
 
∑ GHG emissions of the TCEs 
 
∑ transport activity of the TCEs 
 
 
Hub activities are not taken into account in the 
calculation of the transport activity of the transport 
chain, but their associated GHG emissions are still 
included in the GHG emissions of the transport chain 
and thus also in the GHG emission intensity of the 
transport chain. 
 
ISO 14083 also offers the possibility of adding up GHG 
emissions from different transport chains, e.g. if an 
organisation wants to report on all its transport 
processes. 
5.2 Case examples Part 3 
In the preceding section 4.3, steps 3 and 4 were 
described for the case examples and it was shown 
how the associated GHG emission intensities were 
determined for the transport and hub operations. 
Now follow steps 5 and 6. 
Calculation of  
GHG emissions of a 
transport chain 


---

## Page 48

48 
Calculation of GHG emissions of a transport 
chain 
 
 
 
 
 
 
Case example A: Transport services in freight transport (continued from page 44) 
 
The previous section 4.3 showed how the associated GHG emission intensities were determined for the 
transport service in freight transport for the different transport and hub operation categories.  
 
Step 5: Calculation of the GHG emissions of the TCEs  
With the help of this information and the transport/hub operations from Section 3.3, the GHG emissions 
of the individual tran sport chain elements can now be calculated in step 5 according to the above 
formula. 
 
▸ GHG emissions TCE 1: 0.150 kg CO2e/tkm x 500 tkm = 75.0 kg CO2e 
 
▸ GHG emissions TCE 2: 1.07 kg CO2e/t x 10 t = 10.7 kg CO2e 
 
▸ GHG emissions TCE 3: 0.014 kg CO2e/tkm x 5,000 tkm = 71.9 kg CO2e 
 
▸ GHG emissions TCE 4: 1.07 kg CO2e/t x 10 t = 10.7 kg CO2e 
 
▸ GHG emissions TCE 5: 0.150 kg CO2e/tkm x 1,000 tkm = 150 kg CO2e 
 
Step 6: Calculation of GHG emissions and GHG emission intensity of the transport chain  
In the last step, the company now adds up all GHG emissions of TCEs 1 to 5. In addition, it 
determines the transport activity of the entire transport chain, which is made up of the sum of the 
TO of TCEs 1, 3 and 5 and thus amounts to 6,500 tkm. 
 
In order to obtain the GHG emission intensity of the transport chain, the GHG emissions of the 
transport chain are divided by the transport activity of the transport chain:  
 
So the process looks like this: 
 
▸ Total GHG emissions: (75.0 + 10.7 + 71.9 + 10.7 + 150) kg CO2e = 318.3 kg CO2e 
 
▸ GHG emission intensity of TC: 318.3 kg CO2e / 6,500 tkm = 0.049 kg CO2e/tkm 
 
It is important to note that the final GHG emission intensity of the entire transport chain also includes 
the GHG emissions of the intermediate hubs, even if these do not represent a transport process.  

---

## Page 49

49 
Calculation of GHG emissions of a transport chain  
 
 
 
 
Figure 8 
 
Illustration of steps 5 and 6: GHG emissions and GHG emission intensities of the transport chain elements 
and transport chain  
 
Source: own illustration, ifeu/Fraunhofer IML 
 
Case example B: Passenger transport of an organisation (continued from page 46) 
 
Step 5: Calculation of the GHG emissions of the TCEs  
 
In this case example, the GHG emissions of the individual TCEs are not reported (although this is necessary 
according to ISO), as they are calculated according to the same rules as the TOCs.  
 
Step 6: Calculation of GHG emissions and GHG emission intensity of the transport chain  
 
In order to calculate the GHG emissions of the transport chain(s) (and thus also the organisation's annual GHG 
emissions from its passenger transport by bus), the GHG emissions of TOC A, TOC B and TOC C can be summed up. 
The resulting total of 1,325,464 kg CO2e (of which 962,917 kg CO2e from operations) can now be divided by the 
total transport activities of 16,902,000 pkm to obtain the GHG emission intensity of passenger transport. This is 78 
g CO2e/pkm (of which 57 g CO2e/pkm from operations). 
 


---

## Page 50

50 
 
 
 
 
 
 
6 Reporting according to ISO 14083 
 
Reporting is an integral part of any GHG emissions 
calculation in accordance with ISO 14083, which is 
why ISO 14083 contains requirements for the scope of 
reporting and specifies what further information must 
be reported. 
 
Uniform and transparent reporting enables the 
exchange of information between different partners 
along a transport chain and supports the further use of 
calculation results, e.g. in other calculations. It also 
enables a comparison between different transport 
chains and organisations. However, it is essential that 
all relevant framework conditions and assumptions 
that significantly influence the results are clearly 
documented. For this purpose, ISO 14083 has 
formulated clear requirements, which are summarised 
below. 
 
The report can be established from two different 
perspectives: at the level of transport or hub services 
or at the level of an organisation. The reporting 
organisation can also decide – regardless of the 
reporting level chosen – whether to produce a single 
report containing all the necessary information or 
only a short report, which is supplemented by 
additional information elsewhere (e.g. reference to 
the webpage). In the following, therefore, the 
minimum disclosures (short report) and the 
additional information will be discussed in more 
detail. Together, the two make up the ISO-compliant 
report. 
 
6.1 Short reports 
Short report at the level of transport or hub services 
In the case of a report at the level of transport or 
hub services, the information refers to one or more 
transport chain elements. If the report includes 
several transport chain elements, they can represent 
a complete transport chain or only part of it. The 
following table summarises all the reporting 
elements of a short report. This should be 
supplemented by additional information (see 
Section 6.2). 
 
Short report at the organ isational level 
The information of a short report at organizational  
relates either to all transport chains or to a part of 
them, regardless of whether they are operated or 
purchased by the organisation itself. The report itself 
can be divided by organisational structure, such as 
business units, regions, or subsidiaries. In this case, 
ISO 14083 recommends that the organisation prepare 
at least one annual report covering all operations in 
twelve consecutive months. This report may be 
supplemented by reports on shorter periods and/or 
selected journeys and operations. 
6 
Reporting according 
to ISO 14083 

---

## Page 51

Reporting according to ISO 14083  
51 
 
 
 
 
 
Table 10 
 
Note: The abbreviations/formula symbols are listed in the glossary.  
* GHG emissions from the operation of a vehicle ( GVO) are also known as TTW emissions and can be classified as Scope 1 or Scope 3 emissions under the 
GHG Protocol , depending on who is responsible for the operation and who wants to report the GHG emissions.  
 
 
Table 11 
Elements of the short report at organisational level  
Report elements Description 
Identification of the services 
covered 
Indication of which transport chains are covered in the report, 
if necessary, breakdown according to the organisational 
structure 
Reference to ISO 14083 Reference to ISO 14083:2023 
Results on GHG emissions 
and GHG emission intensities 
From operation and energy provision (GT) or (gT) 
1. across all transport chains 
2. across all TCEs of one transport mode and for hub operations 
Optional: supplemented by corresponding values for GHG emissions from 
operation 
Transport activity distance Indication of the type used (i.e. SFD or GCD) (per transport mode) 
Additional information Reference to the location where additional information is published 
Elements of the short report at the level of transport or hub services  
Report elements Description 
Identification of the services 
covered 
Identification of which transport chains or which transport chain elements are 
covered in the report, based on an exhaustive list of services or indication of 
the period of time. 
Reference to ISO 14083 Reference to ISO 14083:2023 
Overall result on GHG 
emissions and GHG emission 
intensities 
Total sum, i.e. sum of all TCE 
(1) from operation and energy provision (GT,TC) or gT,TC and 
(2) from operation (GVO,TC or GHEO,TC) or (gVO,TC or gHEO,TC)* 
Transport activity Total sum, i.e. sum of all transport TCEs 
Transport activity distance Indication of the type used (i.e. SFD or GCD) (per transport mode) 
Hub activity Sum over all hub TCEs 
Partial results per transport 
mode and hub 
For each mode and for hub operations 
(1) Total GHG emissions and transport activity 
and/or 
(2) GHG emission intensities 
Additional information Reference to the location where additional information is published 

---

## Page 52

Reporting according to ISO 14083  
52 
 
 
 
6.2 Additional information as part of the 
reporting 
The short reports are only part of the complete 
reporting in accordance with ISO 14083. A 
complete presentation of the results requires 
additional information that is easily accessible, 
clearly structured and transparent with regard to 
data acquisition and calculation. In the following, 
guiding questions are formulated on the basis of 
which the reporting organisation can decide 
whether and which additional information it wants 
or must publish in order to report in accordance 
with ISO 14083. 
 
Are all relevant processes included in the calculation? 
In principle, none of the processes, inputs or outputs 
described above must be omitted. If this is the case, 
the report must explain this decision and the reasons 
and consequences for omitting it, supplemented by 
any cut-off criteria used (see also Section 2.1). 
 
When calculating GHG emissions of hub operations, 
the reporting organisation may be faced with the task 
of assigning energy consumed by vehicles or vessels 
temporarily operated in a hub to transport operation 
(see Table 2). If these are assigned to the hub 
operations, this must be reported transparently. 
ISO 14083 also makes it possible to include optional 
processes in the GHG emissions calculation. This 
includes, for example, GHG emissions associated with 
the storage and (re)packaging of goods in logistics 
hubs, or those generated by the use of information 
and communication technology (ICT) equipment and 
external data servers. If these optional aspects have 
also been calculated, this must be clearly stated in the 
report. The separate identification (subtraction) of the 
optional components is not required. 
 
Where was primary data not used?  
Only if no primary data is available for a n operation, 
secondary data, i.e. modelled data or default values, 
may be used in the GHG emission calculation. The use 
of secondary data must be justified and documented. 
 
Has data been model led or have default values been used? 
When using secondary data, ISO 14083 requires the 
use of tabular documentation for reporting (see Table 
12). The table contains basic influencing parameters 
of the modelling and may be extended accordingly by 
additional relevant input parameters if necessary. For 
each model used, the reporting organisation must 
complete the table below and make it available upon 
request. 
 
Table 12 
Reporting when using secondary data  
Input parameters of m odelling and use of deviating default GHG emission intensities 
 
Model type  
 Energy based modelling Yes/No 
 Activity based modelling 
 
Yes/No 
 
Parameter Included 
Yes/No 
Additional information 
If included, state predominant input 
data type 
Vehicle fleet related 
Vehicle class/fleet profile Yes/No/Not applicable Primary/modelled/default 
Energy consumption profile Yes/No/Not applicable Primary/modelled/default 
Vehicle configuration Yes/No/Not applicable Primary/modelled/default 
Body type/empty vehicle mass Yes/No/Not applicable Primary/modelled/default 
Engine type Yes/No/Not applicable Primary/modelled/default 
Engine emission class Yes/No/Not applicable Primary/modelled/default 

---

## Page 53

Reporting according to ISO 14083  
 
53  
Parameter Included 
Yes/No 
Additional information 
If included, state predominant input 
data type 
Energy carrier(s) used in vehicle Yes/No/Not applicable Primary/modelled/default 
Share of energy carrier Yes/No/Not applicable Primary/modelled/default 
Operational 
Freight type Yes/No/Not applicable Primary/modelled/default 
Freight requirements (e.g. 
temperature control, hazardous) Yes/No/Not applicable Primary/modelled/default 
Use of specific container type Yes/No/Not applicable Primary/modelled/default 
Load factor or average load 
expressed in tonnes Yes/No/Not applicable Primary/modelled/default 
Service type (e.g. full 
truckload/less than truckload, 
full container load/ less than 
container load 
Yes/No/Not applicable Primary/modelled/default 
Extent of empty trips Yes/No/Not applicable Primary/modelled/default 
Journey characteristics 
Routing, including location of 
intermediate stops Yes/No/Not applicable Primary/modelled/default 
Route characteristics Yes/No/Not applicable Primary/modelled/default 
Direct/via location/multiple 
collection and delivery Yes/No/Not applicable Primary/modelled/default 
Drive cycle Yes/No/Not applicable Primary/modelled/default 
Road type/ channel type Yes/No/Not applicable Primary/modelled/default 
Urban/mixed/long haul Yes/No/Not applicable Primary/modelled/default 
Frequency of stops Yes/No/Not applicable Primary/modelled/default 
Speed profile Yes/No/Not applicable Primary/modelled/default 
Topography Yes/No/Not applicable Primary/modelled/default 
Geographic region of 
applicability Yes/No/Not applicable Primary/modelled/default 
Current/flow rate/head, cross or 
tail wind and windspeed Yes/No/Not applicable Primary/modelled/default 
Additional items  
…   
Source: DIN EN ISO 14083, Tabl e 3 
 

---

## Page 54

Reporting according to ISO 14083  
54 
 
 
 
If default values are used, their source must be 
reported. Unless the sources recommended by ISO 
14083 in Annex Q have been selected (see Annex A.5 
in the guide), the alternative source selection must be 
justified. When selecting the default values, the best 
correspondence between the standard classification of 
GHG emission intensity and the mode-specific 
characteristics of a TOC or HOC should be achieved. If 
no clear matching is possible, the selected sources 
must be documented, as well as the reasons for the 
selection. 
 
How were emissions allocated, if any ? 
The reporting must transparently document the 
selected allocation method (e.g. area-based allocation 
key, see examples in Section 4.2.2). 
Which emission factors were used?  
The fuels considered in the GHG emission calculation must 
be transparently documented together with their GHG 
emission factors. The respective source must also be listed. 
 
These requirements, which result from Annex J.4 of 
ISO 14083, can be problematic for reporting 
organisations if they use licensed GHG emission 
factors that are not allowed to be published under 
the licence agreement. In these cases, the authors 
recommend filling out the table as far as possible and 
otherwise referring to the external "licensed data". 
By providing clear, i.e. reproducible, source 
information, it is possible for those who also hold a 
licence to reproduce the GHG emission factor. 
 
Table 13 
 
Documentation of the emission factors of fuels and electricity  
Fuel type Lower 
heating 
value 
Density 
(1) 
Operational 
GHG emissions  
Total GHG 
emissions 
(2) 
Biofuel blend 
(%energy 
content)  
Source 
 [MJ/kg] [kg/l] [g CO2e/MJ] [g CO2e/MJ]   
       
       
(1) for liquid fuels;  (2) from the operation and energy provision   
 
With regard to biofuels, ISO 14083 recommends that 
GHG emissions from indirect land use change (iLUC) 
be reported separately in the report and that the 
sources used are transparently documented incl. 
assumptions. 
 
GHG emission factors for energy provision must also 
include the infrastructure of the energy carriers. If the 
best available data sources do not contain them, this 
must be documented. This can be done, for example, 
in tabular documentation. 
 
In the case of electricity generation, ISO 14083 allows 
for a separate quantification of GHG emissions from 
infrastructure. These may be documented separately 
and included in the report. 
If an organisation has also used its own electricity mix for 
its electricity consumption according to the market-based 
approach, the GHG results must be documented and 
reported separately from the calculations with the 
national electricity mix. If the GHG emission results are to 
be used for further use in calculations for the Product 
Carbon Footprint in accordance with ISO 14067, the 
market-based electricity mix must also be disclosed in the 
report. 
 
The IPCC's latest publication on global warming 
potentials (GWP) is – at the time of publication of this 
guide – the sixth assessment report (Smith et al. 
2021). The source used must be documented 
transparently. The use of deviating GWP (time 
horizon of 100 years, without climate-carbon 
feedback) should be explained. 

---

## Page 55

Reporting according to ISO 14083  
55 
 
 
 
 
Were alternative units of transport or hub activity 
used? 
ISO 14083 specifies tonnes as the standard unit for 
transport and hub activities for freight. For some 
operations, such as mail and parcel operations and 
containerised freight, the standard allows for an 
alternative unit. The choice of an alternative unit is to 
be justified and documented in the report. Examples 
of conversion factors are given in Annex A.1. 
Are there any national requirements that deviate from 
ISO 14083? 
Requirements from national and international 
legislative bodies take precedence over ISO 14083, 
and if they require the use of a specific quantification 
methodology and/or the use of specific GHG emission 
factors, the methodology and sources of the GHG 
emission factors must be clearly documented in the 
report. 
 
6.3 Case examples Part 4 
 
Table 14 
Short report on the Case example A 
Report element Description 
Identification of the 
services covered Final transport chain  
Reference to ISO 14083 These calculation results were calculated in accordance with ISO 14083:2023. 
Overall results on GHG 
emissions  
Total GHG emissions of the transport chain: 
GT,TC = 318.3 kg CO2e (of which 296.9 kg CO2e from road/rail and 21.4 
kg CO2e from the hub) 
GHG emissions from the operation of the transport chain: 
GO,TC =170 kg CO2e (of which 162 kg CO2e from the road and 8 kg CO2e from the hub) 
Overall results on GHG 
emission intensities 
Total from operation and energy provision: gT,TC = 0.049 kg CO2e/tkm 
Total from operation: gO,TC = 0.022 kg CO2e/tkm 
Transport activity of the 
TC 6,500 tkm (sum of all transport TCEs) 
Transport activity distances 
Road (TCE 1 and TCE 5): SFD  
Rail (TCE 3): SFD 
Hub activity 20 t (sum of all hub TCEs) 
GHG emission intensities 
by transport mode and 
hub* 
Road (TCE 1, TCE 5): 0.150 kg CO2e/tkm 
Rail (TCE 3): 0.014 kg CO2e/tkm 
CT terminal (TCE 2, TCE 4): 1.07 kg CO2e/t 
Additional information subsequent 
*The TCE numbers shown are supplemented for illustrative purposes only for this example and are not generally required in rep orting. 
 
Case example A: Transport services in freight transport (continued from page 50) 
Reporting for Case example A is carried out at the level of the transport service. For this purpose, a short report 
in tabular form is first prepared. The necessary additional information is then compiled, which can be published 
together with the summary report or separately. 

---

## Page 56

Reporting according to ISO 14083  
56 
 
 
 
 
 
Table 15 
 
Reporting for the use of secondary data in Case example A for TCEs 1, 3 and 5  
Input parameters of modelling and use of deviating default GHG emission intensities   
 
 
Parameter Included 
Yes/No 
Additional information 
If included, state predominant input 
data type 
Vehicle fleet related 
Vehicle class/fleet profile Yes (for road) Modelled 
Energy consumption profile Yes Modelled 
Vehicle configuration Yes (for road) Modelled 
Body type/empty vehicle mass Yes (for road) Modelled 
Engine type Yes (for road) Primary 
Engine emission class Yes (for road) Primary 
Energy carrier(s) used in vehicle Yes Primary 
Share of energy carrier Yes Primary 
Operational 
Freight type Primary Primary 
Freight requirements (e.g. 
temperature control, hazardous) 
Not applicable (ambient 
temperature) Primary 
Use of specific container type Yes Primary 
Load factor or average load 
expressed in tonnes Yes Primary (road) / modelled (rail) 
 
▸ Are all relevant processes included in the calculation?  
Yes, which means no further documentation is required. 
 
▸ At what point were secondary data used instead of primary data?  
Different data categories were used for the individual TCE in the GHG emission calculation, i.e. 
modelled data for transport in TCE 1, TCE 3 and TCE 5, and default values of transhipment in TCE 2 
and TCE 4. The documentation of the model is shown in Table 15. A default value according to GLEC 
Framework Version 3 was used for handling at the CT terminal. 
 
▸ An allocation was not required in the case example and therefore does not need to be documented. 
 
▸ Which GHG emission factors were used? 
GHG emission factors for diesel and electricity were used in the GHG emission calculation. At this 
point, reference should be made to Annex A.3 of the guide. A default value according to GLEC 
Framework Version 3 was used for handling at the CT terminal.  

---

## Page 57

Reporting according to ISO 14083  
57 
 
 
Parameter Included 
Yes/No 
Additional information 
If included, state predominant input 
data type 
Service type (e.g. full 
truckload/less than truckload, 
full container load/ less than 
container load 
Yes Primary 
Extent of empty trips Yes Default 
Journey characteristics 
Routing, including location of 
intermediate stops Yes Primary 
Route characteristics Yes Modelled 
Direct/via location/multiple 
collection and delivery Yes (direct) Primary 
Drive cycle Yes (road) Modelled 
Road type/ channel type 
Yes (road type) 
Not applicable (channel type) 
Modelled 
Urban/mixed/long haul Yes (road) Modelled 
Frequency of stops No  
Speed profile Yes (road) Modelled 
Topography Yes (road) Modelled 
Geographic region of applicability Yes Primary 
Current/flow rate/head, cross or 
tail wind and windspeed No  
Additional items  
CT terminal Yes Default 
 
 
 

---

## Page 58

Reporting according to ISO 14083  
58 
 
 
 
 
 
Table 16 
Short report on the Case example B  
Report element Description 
Identification of the 
services covered 
All transport chains of the organisation (passenger transport by bus) within one 
calendar year 
Reference to ISO 14083 These calculation results were calculated in accordance with ISO 14083:2023. 
Overall results on GHG 
emissions 
Total GHG emissions of the transport chain: 
GT,TC = 1,371,631 kg CO2e (of which 1,279,339 kg CO2e from diesel and 
92,292 kg CO2e from electricity) 
GHG emissions from the operation of the transport chain: 
GO,TC =962,917 kg CO2e (all from diesel) 
Overall results on GHG 
emission intensities 
Total of operation and energy provision: gT,TC = 0.080 kg CO2e/pkm  
Total from operation: gO,TC = 0.056 kg CO2e/pkm 
Transport activity 17,064,000 pkm (sum of all transport TCEs) 
Transport activity 
distances 
SFD 
Additional information subsequent 
 
Case example B: Passenger transport of an organisation (continued from page 51) 
 
Reporting for Case example B is established at the level of the organi sation. For this purpose, a short tabular 
report is prepared first. The necessary additional information is then compiled, which can be published 
together with the summary report or separately. 
  
▸ Are all relevant processes included in the calculation? 
Yes, which means no further documentation is required. 
 
▸ At what point were secondary data used instead of primary data?  
For the organisation's bus fleet, primary data were available for both trans port activity and GHG 
activities. Thus, no secondary data had to be used. 
 
▸ An allocation was not required in the case example and therefore does not need to be documented. 
 
▸ Which GHG emission factors were used? 
GHG emission factors for diesel and electricity were used in the GHG emission calculation. At this point, 
reference should be made to Annex A.3 of the guide. 

---

## Page 59

 
 
References 
 
References 
 
 
ADEME (2023): Bilans GES: Centre de ressources sur les bilans de 
gaz à effet de serre. https://bilans-ges.ademe.fr (14.12.2023). 
DIN EN ISO 14083 (2023): Treibhausgase – 
Quantifizierung und Berichterstattung über 
Treibhausgasemissionen von Transportvorgängen (ISO 
14083:2023); German version DIN EN ISO 14083:2023. 
https://dx.doi.org/10.31030/3447231. 
Dobers, K.; Jarmer, J. -P. (2023): Guide for Greenhouse 
Gas Emissions Accounting at Logisti cs Hubs. DOI: 
10.24406/ publica-2261. 
Dobers, K.; Perotti, S.; Jarmer, J.-P.; Fossa, A.; Romano 
S. (2023a): Sustainability and GHG performance at logistics 
hubs. Webinar. https://www.etp-logistics.eu/sustainability-
and-ghg- performance-at-logistics-hubs/ (12.10.2023). 
Dobers, K.; Perotti, S.; Wilmsmeier, G.; Mauer, G.; Jarmer, J. -
P.; Spaggiari, L.; Hering, M.; Romano, S.; Skalski, M. (2023b): 
Sustainable logistics hubs: greenhouse gas emissions as one 
sustainability key performance indicator. In: Transportation Research 
Procedia. Vol. 72, pp. 1153–1160. DOI: 10.1016/y. 
trpro.2023.11.572. 
Dobers, K.; Zimmermann, T.; Jarmer, J. -P. (2023c): REff 
Assessment Tool. In: REff Tool®, the GHG assessment Tool for 
logistics sites. Dortmund. https://reff.iml.fhg.de/. (14.12.2023). 
EcoTransIT World (2023): Environmental Methodology and 
Data - Update 2023. https://www.ecotransit.org/wp-content/ 
uploads/20230612_Methodology_Report_Update_2023.pdf 
(06.12.2023). 
EN 16258 (2012): Methodology for calculation and declaration of 
energy consumption and GHG emissions of transport services 
(freight and passengers). 
Energy Conservation Centre Japan (2023) : Act on the Rational 
Use of Energy. The Energy Conservation Centre Japan. 
https://www.enecho.meti.go.jp/category/saving_and_new/
saving/enterprise/overview/laws/index.html (14.12.2023). 
European Commission (2023): European Commission 
COM/2023/441 final Vorschlag für eine VERORDNUNG DES 
EUROPÄISCHEN PARLAMENTS UND DES RATES über die 
Erfassung der Treibhausgasemissionen von Verkehrsdiensten 
11.07.2023. https://eur-lex.europa.eu/legal-
content/EN/TXT/?uri=celex%3A52023PC0441 (14.12.2023). 
European Parliament (2018): Directive (EU) 2018/2001 of the 
European Parliament and of the Council of 11 December 2018 on 
the promotion of the use of energy from renewable sources (recast) 
(Text with EEA relevance.). https://eur-lex.europa.eu/legal-
content/EN/TXT/PDF/?uri=CELEX:32018L2001(14.12.2023). 
Fuel EU maritime (2021): Proposal for a REGULATION OF THE 
EUROPEAN PARLIAMENT AND OF THE COUNCIL on the use of 
renewable and low-carbon fuels in maritime transport and amending 
Directive 2009/16/EC. https://eur-lex.europa.eu/legal-
content/EN/TXT/HTML/?uri=CELEX%3A52021PC0562 (17.01.2024). 
INFRAS (2023): Handbook on Emission Factors for Road Transport 
(Software, Version 4.2). https://www.hbefa.net. 
 
IPCC (2023): Climate Change 2021 – The Physical Science Basis: 
Working Group I Contribution to the Sixth Assessment Report of the 
Intergovernmental Panel on Climate Change. Cambridge University Press, 
Cambridge. DOI: 10.1017/9781009157896. 
John Beath; Nyx Black; Marjorie Boone; Guy Roberts; 
Brandy Rutledge; Amgad Elgowainy; Michael Wang; Jarod 
Kelly (2014): Contribution of Infrastructure to Oil and Gas 
Production and Processing Carbon Footprint. 
https://greet.anl.gov/files/oil-gas-prod-infra (06.12.2023). 
Myhre, G.; Shindell, S.; Bréon, F. M.; Collins, W.; 
Fuglestvedt, J.; Huang, J.; Koch, D.; Lamarque, J. -F.; Lee, 
D.; Mendoza, B.; Nakajima, T.; Roböck, A.; Stephens, G.; 
Takemura, T.; Zhang 
H. (2013): Climate Change 2013: The Physical Science Basis. 
Contribution of Working Group I to the Fifth Assessment Report of 
the Intergovernmental Panel on Climate Change. Cambridge 
University Press, Cambridge; United Kingdom; New York, NY, USA. 
https://www.ipcc.ch/site/assets/uploads/2018/02/WG1AR5_Chapter
08_FINAL.pdf (06.12.2023). 
Ranganathan, J.; Corbier, L.; Bhatia, P.; Schmitz, S.; Gage, 
P.; Oren, K. (2004): The Greenhouse Gas Protocol A Corporate 
Accounting and Reporting Standard (Revised Edition). 
World Resources Institute, Business Council for Sustainable 
Development, USA. https://www.wri.org/research/greenhouse-
gas-protocol-0 (27.04.2023). 
Smart Freight Centre (2019): Global Logistics Emissions Council 
(GLEC) Framework for Logistics Emissions Calculation and Reporting. 
Version 2.0. 
Smart Freight Centre (2024): Global Logistics Emissions Council 
Framework for Logistics Emission Accounting and Reporting; Version 
3.1 edition, revised and updated. 
Smith, C.; Nicholls, Z. R. J.; Armour, K.; Collins, W.; 
Forster, P.; Meinshausen, M.; Palmer, M. D.; Watanabe, 
M. (2021): The Earth's Energy Budget, Climate Feedbacks, and 
Climate Sensitivity. Cambridge University Press, Cambridge, 
United Kingdom; New York, NY, USA. 
https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_
AR6_WGI_Chapter07.pdf (06.12.2023). 
UK Government (2022): Greenhouse gas reporting: conversion 
factors 2021. https://www.gov.uk/government/publications/ 
greenhouse-gas-reporting-conversion-factors-2021 (14.12.2023). 
vom Wagner Berg, B.; Arens, U.; Kühne, U., Stenau, J. P. 
(2023): NOW Studie: Klimafreundliche Kühlsysteme für den 
Straßengüterverkehr. https://www.now-gmbh.de/wp-content/ 
uploads/2023/07/NOW-Studie_Klimafreundliche-
Kühlsysteme-fuer-den-Strassengueterverkehr.pdf 
(14.12.2023). 
World Resource Institute; World Business Council for 
Sustainable Development (2011): Greenhouse gas protocol. 
Corporate value chain (Scope 3) accounting and reporting standard: 
supplement to the GHG protocol corporate accounting and reporting 
standard. Washington DC, Geneva. 
https://ghgprotocol.org/sites/default/ files/standards/ghg-
protocol-revised.pdf (19.01.2024). 
 
 
 
 

---

## Page 60

Appendix 
60 
 
 
A Appendix 
A.1. Relevant conversion factors 
▸ 1 kWh = 3.6 MJ 
 
Starting value, unless specific values are available: 
 
▸ 1 TEU = 10 t (Smart Freight Centre 2024) 
▸ 1 pallet = 300 kg (Dobers and Jarmer 2023) 
▸ Table 3: Distances and distance adjustment factors 
▸ Table 5: Passenger equivalents of Ro-Pax ferries 
and trains 
 
 
A.2. TOC characteristics of the different 
modes of transport 
TOC characteristics for air transport according to 
ISO 14083 Table A.1 
 
▸ Journey length: "short (e.g. < 1,500 km)" OR 
"long (> 1,500 km)" 
▸ Plane configuration: "Passenger aircraft without 
cargo" OR "Dedicated freight aircraft" OR 
"Passenger aircraft with belly freight" 
 
TOC characteristics for freight on inland waterway 
vessels according to ISO 14083 Table C.1 
 
▸ Freight type: "Dry bulk" OR 
"Liquid bulk" OR "Containerised" OR 
"Mass-limited, general freight" OR 
"Volume-limited, general freight" 
▸ Vessel size category: "< 50 m" OR 
"50 m to 80 m" OR "80 m to 110 m" OR 
"110 m to 135 m" OR "> 135 m" 
▸ Vessel configuration: "Individual vessel" OR 
"Pushed convoy" 
▸ Condition: "Ambient " OR  
"Temperature controlled" 
▸ Waterway type: "Canal" OR "River" OR "Lake"
 
 
TOC characteristics for passengers on inland 
waterway vessels according to ISO 14083 Table C.2 
 
▸ Vessel operation type: "River cruise" OR 
"Ro-Pax river ferry" OR "Waterbus" OR 
"Water taxi" 
▸ Vessel size category: “Varies by vessel type” 
▸ Condition: "Transport only" OR "Transport plus other 
services (restaurant, accommodation, etc.)" 
▸ Waterway type: "Canal" OR "River" OR "Lake" 
 
TOC characteristics for rail freight transport 
according to ISO 14083 Table E.1 
 
▸ Operation type: "Long-distance freight transport: 
block train" OR "Long-distance freight transport: 
single wagon" OR " Long-distance freight 
transport: intermodal wagon” OR “Short-distance 
freight transport (feeder transport)" 
▸ Freight type: "Average/mixed" OR 
"Containerised/swap bodies" OR "Dry bulk" OR 
"Liquid bulk" OR "Vehicle transport" OR "Semi-
trailers" OR "Other" 
▸ Condition: "Ambient" OR "Temperature-controlled" 
▸ Propulsion: "Electric motor: fixed electricity supply 
system (catenary, third rail)" OR "Electric motor: 
on train battery energy storage" OR "Electric 
motor: fuel cell energy storage" OR "Combustion 
engine" OR "Other" 
 
TOC characteristics for rail passenger transport 
according to ISO 14083 Table E.2 
 
▸ Train operation type: "Long-distance passenger trains" OR 
"Short-distance passenger trains" OR "Urban passenger: 
suburban trains" OR "Urban passenger: tram (streetcar)" OR 
"Urban passenger: underground (subway, metro)" 

---

## Page 61

Appendix 
61 
 
 
 
▸ Passenger experience: "Night trains (slow trains)" 
OR "Vehicle trains (slow trains)" OR "Luxury trains 
(slow trains)" OR "High-speed trains" OR "Other" 
▸ Propulsion: "Electric motor: fixed electricity supply 
system (catenary, third rail)” OR "Electric motor: 
on train battery energy storage" OR "Electric 
motor: fuel cell energy storage" OR "Combustion 
engine" OR "Other" 
 
TOC characteristics for road freight transport 
according to ISO 14083 Table F.1 
 
▸ Freight type: "Dry bulk" OR "Liquid bulk" OR 
"Containerised" OR "Palletised" OR "Mass-
limited, general cargo (heavy cargo)" OR 
"Volume-limited, general cargo (light cargo)" 
OR "Vehicle transport" 
▸ Condition: "Ambient " OR " temperature-controlled" 
▸ Journey type: "Point-to-point (long haul)" OR 
"Collection and delivery" 
▸Contract type: "Shared transport" OR "Dedicated 
contract (charter)" 
 
TOC characteristics for road passenger transport 
according to ISO 14083 Table F.2 
 
▸ Means of transport: "Shared public transport (e.g. 
bus, coach, trolleybus)" OR "Shared private 
transport (taxi)" OR "Private transport (e.g. own 
car, bicycle, scooter, motorbike)" 
▸ Journey type: "Urban" OR "Suburban" OR 
"Regional" OR "Long-distance" OR "Dedicated 
lines (e.g. school bus)" 
▸ Level of passenger loading: "Discrete number of 
individuals (1, 2, 3, etc.)" OR "Average occupancy 
rate" 
 
TOC characteristics for cargo on seagoing vessels 
in accordance with ISO 14083 Table G.1 
 
▸ Vessel type: "Bulk carrier" OR "Chemical tanker" OR 
"General cargo" OR "Ro-Ro (roll-on roll-off freight)" 
OR "Liquefied gas tanker" OR "Oil tanker" OR “Other 
liquid tanker” OR “Container” OR “Vehicle carrier” 
▸ Freight condition: "Ambient" OR "Temperature-
controlled" OR "Mixed ambient and temperature-
controlled" 
▸ Service type: "Scheduled (by origin and destination 
pairs)" OR "Tramp" 
 
TOC characteristics for passengers on seagoing 
vessels according to ISO 14083 Table G.2 
 
▸ Vessel type: "Passenger ferry" OR "Cruise ship"  
▸ Vessel size: “Varies by vessel type  
(more information in ISO 14083 Table G.4) 
▸ Service type: "Scheduled (by origin and destination 
pairs)" OR "Chartered" 
 
TOC characteristics for mixed passenger and 
cargo on seagoing vessels in accordance with ISO 
14083 Table G.3 
 
▸ Vessel type: "Ro-Pax ferry (mixture of roll-on 
roll-off freight and passengers)" 
▸ Vessel size: “Varies by vessel type” 
(more information in ISO 14083 Table G.4) 
▸ Service type: "Scheduled (by origin and 
destination pairs)" OR "Chartered" 
 
 
A.3. GHG emission factors of common energy 
carriers 
As part of the work on this guideline, it was not 
possible to carry out our own analyses for GHG 
emission factors of energy carriers. However, the 
factors listed in the informative annex to ISO 14083 
are considered obsolete according to recent findings 
on increased methane emissions from oil and natural 
gas extraction. For this reason, the GHG emission 
factors of the most common European energy 
carriers have been analysed here based on the work 
for the EcoTransIT World Tool (EcoTransIT World 
2023). These factors were also used for the 
calculations in the case examples. 

---

## Page 62

Appendix 
62 
 
 
 
Table 17 
 
GHG emission factors of European energy carriers 
 
* In this column, the CO 2 emissions from operation are also 
given, since they are only influenced by the energy carrier and 
not by its use. 
Source: own calculations, ifeu Institute for EcoTransIT World 
and GHG emissions energy supply from ecoinvent 3.9.1 for 
gasoline, diesel, kerosene and HFO 
Energy 
carrier  
Lower 
heating value  
[g CO2e/MJ] 
Density 
(kg/l) 
GHG 
emissions 
operation  
[g CO2e/MJ]  
GHG 
emissions 
energy 
provision 
(g CO2e/MJ) 
Total GHG 
emissions  
[g CO2e/MJ]  
Gasoline 42.5  0.743  74.96 (of which 
74.82 from CO2) 
24.01  98.97  
Ethanol (40 % 
corn, 35 % 
sugar-beet, 25 % 
wheat) 
27.0  0.780  0.14 (of which 0 
from CO2) 
47.90  48.03  
Diesel  42.8  0.832  75.26 (of which 
74.10 from CO2) 
22.56  97.82  
Diesel with 6.3 % 
biodiesel  
42.4  0.836  70.6  23.22  93.8  
Biodiesel (50 % 
rapeseed, 40 % 
used cooking oil, 
10 % soy) 
37.0  0.892  1.16 (of which  
0 from CO2)  
34.22  35.38  
HVO (50 % 
rapeseed, 50 % 
used cooking oil)  
44.0  0.770  1.16 (of which  
0 from CO2)  
28.56  29.72  
CNG (SI truck)  49.2  -  56.08 (of which 
55.14 from CO2) 
21.04  77.12  
Bio-CNG (40 % 
corn, 40 % 
manure, 20 % 
organic waste) 
(Truck with 
gasoline engine) 
50.0  -  0.93 (of which  
0 from CO2)  
24.72  25.65  
LNG (SI truck)  49.1   57.35 (of which 
56.42 from CO2) 
25.77  83.12  
LNG sea ship (SI 
engine, dual-
fuel, medium 
speed) 
49.1  -  74.10 (of which 
56.42 from CO2) 
25.77  99.87  
Kerosene  43.0  0.800  74.15 (of which 
73.49 from CO2)  
20.00  94.13  
Heavy fuel Oil 
(HFO) (2.7 % S-
content)  
41.2  0.970  77.06 (of which 
75.73 from CO2) 
16.89  93.95  
Very low sulphur 
fuel oil (VLSFO) 
(0.5 % S-content)  
41.3  0.975  78.87 (of which 
77.54 from CO2) 
20.84  99.85  
Ultra-low sulphur 
fuel oil (ULSFO) 
(0.1 % S content)  
41.1  0.939  78.87 (of which 
77.54 from CO2) 
20.43  99.30  
Consumption 
mix DE 2021 
(Medium voltage) 
-  -  0  123  123  
Consumption 
mix DE 2021 (at 
train pantograph)  
-  -  0  131  131  

---

## Page 63

Appendix 
63 
 
 
 
 
Notes on the table: 
 
▸ GHG emissions from operation comprise of CO2 emissions from operation and non-CO2-GHG emission from 
operations. Since non-CO2-GHG emissions depend not only on the fuel type but also on the intended use, the 
(fossil) CO2 emissions are also shown separately here as information. 
 
▸ To calculate the non-CO2-GHG emissions from operation, a specific vehicle configuration was selected, i.e. a 
gasoline LNF (light commercial vehicle) N1-III Euro 6ab, a diesel tractor-trailer40 t Euro 6a-c, a CNG or LNG 
tractor-trailer 40 t Euro 6a-c (with gasoline engine), an aircraft for kerosene and a seagoing vessel for 
HFO/USLFO/VLSFO. 
 
▸ The high non-CO2-GHG emissions of the LNG seagoing vessel result from the relatively high methane slip of the 
gasoline engine used. At medium speed, they amount to 3.1 mass-percent of the fuel used (Fuel EU maritime 
2021). 
 
Table 18 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(1) market for heat, from steam, in chemical industry (RER); 
(2) own calculation, Fraunhofer IML based on District heating (46 % natural gas, 54 % 
hard coal) (Europe without Switzerland) 
Note: values in the table may differ from the original German version of the guide which 
contained some errors. Values in the table above have been checked and revised. 
Source: ecoinvent 3.9.1 cut-off, IPCC 2021 
A.4. GHG emission factors of common refrigerants 
ISO 14083 recommends using the current GWP values published by the IPCC with a time horizon of 100 years. 
This is the 6th Assessment Report (Smith et al. 2021) at the time of publication of this guide, but it is not yet 
widely applied in tools and reports. For this reason, the following table shows the GWP values from the current, 
sixth (AR6) and the previous, fifth (AR5) assessment report. The GWP values of mixtures are calculated 
accordingly with the specified parts. 
Focus on heating at hubs: GHG emission factors of European energy carriers 
Energy carrier 
Lower calorific 
value  
 
[MJ/kg] 
Density  
 
 
[kg/l] 
GHG 
emissions 
operation 
[g CO2e/MJ] 
GHG emissions 
energy 
provision  
[g CO2e/MJ] 
Total GHG 
emissions  
 
[g CO2e/MJ] 
Process steam (1) 
(4 atm, 140 °C) 
2.74 - 0 110.42 110.42 
District heating (2) - - 0 106.12 106.12 
Natural gas  
at boiler <100 kW 
Not specified - 55.07 17.99 73.06 
Biogas  
at boiler <100 kW 
Not specified - 0.19 13.73 13.92 
Light fuel oil  
in boiler of 100 kW 
Not specified - 78.93 22.33 101.26 
Wood pellets 
furnace 300 kW 
Not specified - 1.02 11.34 12.36 
Wood chips 
furnace 50 kW 
18.3 - 1.53 4.48 6.01 
 

---

## Page 64

Appendix 
64 
 
 
 
 
 
Table 19 
Exemplary emission factors for refrigerants (in g CO 2e per g refrigerant type)  
Refrigerant type Description IPCC 
2013 
AR5 
IPCC 
2021 
AR6 
R-717 NH3, Ammonia - - 
R-600a C4H10, Isobutane 3.0 0.01 
R-1234yf C3H2F4 // CF3CF=CH2, 2,3,3,3- Tetrafluoro propene 1.0 0.5 
R-744 CO2, Carbon dioxide 1.0 1.0 
R-1234ze(E) C3H2F4 // trans-CF3CH=CHF, (E)-1,3,3,3,-
Tetrafluorpropen 
1.0 1.4 
R-32 CH2F2, Difluoromethane 677.0 771.0 
R-448a Mixture, own calculation: 26 % R-32, 26 % R-125, 20% 
R-1234yf, 21 % R-134a, 7 % R-1234ze(E) 
1,273.5 1,494.4 
R-449A Mixture, own calculation: 25,7 % R-134a, 
25,3 % R-1234yf, 24,7 % R-125, 24,3 % R-
32 
1,281.9 1,504.5 
R-134a CH2FCF3, 1,1,1,2-Tetrafluorethane 1,300.0 1,530.0 
R-407C Mixture, own calculation: 23 % R-32, 25 % R-
125, 52 % R-134a 
1,624.2 1,907.9 
R-22 CHClF2, Chlorodifluoromethane 1,760.0 1,960.0 
R-410A Mixture, own calculation: 50 % R-32, 50 % R-125 1,923.5 2,255.5 
R-407A Mixture, own calculation: 20 % R-32, 40 % R-
125, 40 % R-134a 
1,923.4 2,262.2 
R-542a Mixture, own calculation: 11 % R-32, 59 % R-
125, 30 % R-1234yf 
1,945.1 2,291.6 
R-404A Mixture, own calculation: 44 % R-125, 4 % R-
134a, 52 % R-143a 
3,942.8 4,728.0 
R-507 Mixture, own calculation: 50 % R-125, 50 % R-143a 3,985.0 4,775.0 
R-507A Mixture, own calculation: 50 % R-125, 50 % R-143a 3,985.0 4,775.0 
R-115 CClF2CF3, Chloropentafluoroethane 7,670.0 9,600.0 
 
Further emission factors can be found in the guidelines for 
logistics hubs (Dobers and Jarmer 2023). 
Note: values in the table may differ from the original German 
version of the guide which contained some errors. Values in 
the table above have been checked and revised. 
Source: own calculations, Fraunhofer IML 
based on (Myhre et al. 2013) and 
(Smith et al. 2021). 

---

## Page 65

Appendix 
65 
 
 
 
A.5. GHG emission intensities (transport/hubs) and their sources  
ISO 14083 refers to a selection of sources for default values for GHG emission intensities in Annex Q. The order 
does not represent a preference. 
 
▸ GLEC Framework Version 2.0 (Smart Freight Centre 2019)  
Note: An updated version 3.1 has been published since October 2024 (Smart Freight Centre 2024). 
 
▸ REff Tool®: GHG assessment tool for logistics sites (Dobers et al. 2023c)  
 
▸ France: Base Caron® database (ADEME 2023) 
 
▸ Japan: (Energy Conservation Centre Japan 2023) 
 
▸ United Kingdom (UK Government 2022) 
 
 
 

---

## Page 66

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Download our policy papers 
CLECAT | All positions 
 
Website: www.clecat.org  
LinkedIn: https://www.linkedin.com/company/clecat/ 

---

