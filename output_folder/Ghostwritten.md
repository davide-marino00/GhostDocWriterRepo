# Power BI Model & Report Documentation

*Generated on: 2025-06-19 16:06:02*

## Table of Contents

- [Overview](#overview)
- [Data Model](#data-model)
  - [Relationships](#relationships)
  - [Tables](#tables)
    - [Accounts](#table-accounts)
    - [Campaigns](#table-campaigns)
    - [Contacts](#table-contacts)
    - [Industries](#table-industries)
    - [Opportunities](#table-opportunities)
    - [Opportunity Calendar](#table-opportunity-calendar)
    - [Opportunity Forecast Adjustment](#table-opportunity-forecast-adjustment)
    - [Owners](#table-owners)
    - [Products](#table-products)
    - [Territories](#table-territories)
- [Report Structure](#report-structure)
  - [Report Pages](#report-pages)
    - [Sales Overview](#page-sales-overview)
    - [Win/Loss Ratio Overview](#page-winloss-ratio-overview)
    - [Industries Overview](#page-industries-overview)
    - [Pipeline Trends](#page-pipeline-trends)
    - [Trend Analytics](#page-trend-analytics)
    - [Win/Loss Ratio Insights](#page-winloss-ratio-insights)
    - [Days to Close Insights](#page-days-to-close-insights)
    - [Sales Discounting Insights](#page-sales-discounting-insights)
    - [Revenue Source Breakdown](#page-revenue-source-breakdown)
    - [Q&A Query](#page-qa-query)
    - [Template](#page-template)

---

## <a name="overview"></a>Overview

(Error generating overview: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

---

## <a name="data-model"></a>Data Model

### <a name="relationships"></a>Relationships

The following relationships link the tables:

* `Accounts`.[`IndustrySeq`] -> `Industries`.[`IndustrySeq`]
* `Accounts`.[`TerritorySeq`] -> `Territories`.[`TerritorySeq`]
* `Contacts`.[`AccountSeq`] -> `Accounts`.[`AccountSeq`]
* `Opportunities`.[`AccountSeq`] -> `Accounts`.[`AccountSeq`]
* `Opportunities`.[`CampaignSeq`] -> `Campaigns`.[`CampaignSeq`]
* `Opportunities`.[`CloseDate`] -> `Opportunity Calendar`.[`Date`]
* `Opportunities`.[`ProductSeq`] -> `Products`.[`ProductSeq`]
* `Opportunities`.[`SystemUserSeq`] -> `Owners`.[`SystemUserSeq`]

---

### <a name="tables"></a>Tables

#### <a name="table-accounts"></a>Table: `Accounts`

(Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Account Name` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Account Number` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `AccountID` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `AccountOwnerSeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `AccountSeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Country` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `IndustrySeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `State or Province` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `TerritorySeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |

---

#### <a name="table-campaigns"></a>Table: `Campaigns`

(Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Campaign` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Campaign Type` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `CampaignSeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |

---

#### <a name="table-contacts"></a>Table: `Contacts`

(Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `AccountSeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Contact` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `ContactSeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Job Title` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |

---

#### <a name="table-industries"></a>Table: `Industries`

(Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Industry` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `IndustrySeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |

---

#### <a name="table-opportunities"></a>Table: `Opportunities`

(Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `AccountSeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `CampaignSeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `CloseDate` | `dateTime` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `DateDiff-Days` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `DaysToClose` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Decision Maker Identified` | `boolean` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Discount` | `double` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Opportunity Created On` | `dateTime` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `OpportunitySeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Probability` | `double` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Probability (raw)` | `double` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `ProductSeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Purchase Process` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Rating` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Sales Stage` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Status` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `SystemUserSeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Value` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |

##### Calculated Columns

**`Blank`** (`string`)

- **Description:** (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})
- **DAX Expression:**
```dax
BLANK()
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Days Remaining In Pipeline`** (`string`)

- **Description:** (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})
- **DAX Expression:**
```dax
IF(Opportunities[Status]="Open", DATEDIFF(TODAY(),Opportunities[CloseDate],DAY),0)
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Days Remaining In Pipeline (bins)`** (`string`)

- **Description:** (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Weeks Open`** (`string`)

- **Description:** (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Measures

**`Close %`**

- **DAX Expression:**
```dax
[Count of Won]/([Count of Won]+[Count of Lost])
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Count of Lost`**

- **DAX Expression:**
```dax
COUNTAX(
			    FILTER(
			        KEEPFILTERS(Opportunities),Opportunities[Status] = "Lost"
			        ),
			    Opportunities[OpportunitySeq]
			    )
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Count of Won`**

- **DAX Expression:**
```dax
COUNTAX(
			    FILTER(
			        KEEPFILTERS(Opportunities),Opportunities[Status] = "Won"
			        ),
			    Opportunities[OpportunitySeq]
			    )
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Forecast`**

- **DAX Expression:**
```dax
([Revenue Won]+[Revenue In Pipeline])
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Forecast %`**

- **DAX Expression:**
```dax
(([Revenue Won]+[Revenue In Pipeline]))/ [Rev Goal]
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Forecast by Win/Loss Ratio`**

- **DAX Expression:**
```dax
[Revenue Open] * [Close %]
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Opportunity Count`**

- **DAX Explanation (Generated):** (No DAX expression found)

**`Opportunity Count In Pipeline`**

- **DAX Expression:**
```dax
CALCULATE (
			        COUNT( Opportunities[Value] ),
			        FILTER (
			            Opportunities,
			            Opportunities[Status] = "Open"
			              --  && Opportunities[PipelineStep] IN { "3-Pipeline", "4-Mandate", "5-Close" }
			        )
			    )
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Revenue In Pipeline`**

- **DAX Expression:**
```dax
VAR Revenue =
			    CALCULATE (
			        SUMX ( Opportunities, Opportunities[Value] ),
			        FILTER (
			            Opportunities,
			            Opportunities[Status] = "Open"
			            && VALUE(LEFT(Opportunities[Sales Stage],1)) >=2
			        )
			    )
			RETURN
			    Revenue + ( Revenue * ( 'Opportunity Forecast Adjustment'[Forecast Adjustment Value] / 100 ) )
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Revenue Open`**

- **DAX Explanation (Generated):** (No DAX expression found)

**`Revenue Won`**

- **DAX Expression:**
```dax
CALCULATE(
			     SUMX(Opportunities, Opportunities[Value]),
			     FILTER(Opportunities, Opportunities[Status] = "Won")
			 )
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Revenue Won Average Deal Size`**

- **DAX Expression:**
```dax
AVERAGEX(Opportunities,[Revenue Won])
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

---

#### <a name="table-opportunity-calendar"></a>Table: `Opportunity Calendar`

(Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Date` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `DAY` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `DaySeq` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `MONTH` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `MONTH NUMBER` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `RELATIVE 07 DAY PERIOD` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `RELATIVE 30 DAY PERIOD` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `RELATIVE DAY` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `RELATIVE MONTH` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `RELATIVE WEEK` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `WEEK` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `YEAR` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `YEAR MONTH` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `YEAR MONTH NUMBER` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `YEAR WEEK` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |

---

#### <a name="table-opportunity-forecast-adjustment"></a>Table: `Opportunity Forecast Adjustment`

(Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Forecast Adjustment` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |

##### Calculated Columns

**`Blank`** (`string`)

- **Description:** (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})
- **DAX Expression:**
```dax
1
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Measures

**`Fcst adj slicer alt text`**

- **DAX Expression:**
```dax
CONCATENATE("Use the slicer to adjust the forecast, current value is ", 'Opportunity Forecast Adjustment'[Forecast Adjustment Value])
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

**`Forecast Adjustment Value`**

- **DAX Expression:**
```dax
SELECTEDVALUE('Opportunity Forecast Adjustment'[Forecast Adjustment], 0)
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

---

#### <a name="table-owners"></a>Table: `Owners`

(Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Manager` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Owner` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `systemuserid` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `SystemUserSeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |

##### Measures

**`Rev Goal`**

- **DAX Expression:**
```dax
VAR RevenueInPipeline =
			    CALCULATE (
			        SUMX ( Opportunities, Opportunities[Value] ),
			        FILTER (
			            Opportunities,
			            Opportunities[Status] = "Open"
			            && VALUE(LEFT(Opportunities[Sales Stage],1)) >=2
			        )
			    )
			VAR BaseGoal =  
			MROUND(([Revenue Won]+ (RevenueInPipeline*.60)),1000000)    
			RETURN
			IF(BaseGoal > 0, BaseGoal, MROUND(([Revenue Won]+ (RevenueInPipeline*.60)),100000))
```
- **DAX Explanation (Generated):** (Error during enrichment for llm_dax_explanation: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

---

#### <a name="table-products"></a>Table: `Products`

(Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Product` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Product Category` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `ProductSeq` | `int64` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |

---

#### <a name="table-territories"></a>Table: `Territories`

(Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}})

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Country` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Region` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `State Or Province` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `Territory` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |
| `TerritorySeq` | `string` | (Error during enrichment for llm_description: Error code: 404 - {'error': {'code': '404', 'message': 'Resource not found'}}) |

---

## <a name="report-structure"></a>Report Structure

_No report-level filters found._

### <a name="report-pages"></a>Report Pages

#### <a name="page-days-to-close-insights"></a>Page: Days to Close Insights

*Internal Name: `ReportSectionf0c8ef19be5e8127c627`, Ordinal: 6*

##### Page Level Filters

- Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter7`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter8`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter5`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter3`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter4`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter2`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter1`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter6`) (Type: N/A, Definition: N/A)

##### Visuals on this Page

**58a44374ac00e20debb7**

- Type: `None`
- Name: `58a44374ac00e20debb7`
- Fields Used: _(None detected)_

**e9f1d24f308635c7b74b**

- Type: `None`
- Name: `e9f1d24f308635c7b74b`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `80f141278d29b6cb5719`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2a170bf94dfa94fe00cd`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `03e3b50852edcc8445ae`
- Fields Used: _(None detected)_

**image**

- Type: `image`
- Name: `4cabbd60f663c913caa5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0b02c936c6d07e06439e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1c53cde851bd3e05e614`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `366b950342acf05f9a1b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `926309858dd9b4272310`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `de3eb39dd654a0ba8fd6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8c90f6765982f4898ada`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f08b9bbcc5486e1e60c0`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `0b02d573ee35221325dd`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cca86295937d77ea8239`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6954b4af41842bdcf262`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `af7099f1b462801e37b5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d96d32462ba6e9257f2a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `422247311a91e33be583`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6c0c40209ce5883633e4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2a709c9eb4f3e382d4da`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `af0038524d6a64320366`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `41260aa39364596d6c28`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cdc83dacf45a230af70c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3908d1c4568dfd613e80`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1248322628ecda260043`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `02d8321218d86db42fa3`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f9b4c5e1751ec2b60507`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0909f4e093367e2122fd`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `56e960b1f9c4bb3aa11e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ff38d5fe3972955ac20f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `77e4c73a5c00b3014436`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `403efab41564dca9fedf`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `92dea114ade90f95f4a9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `61c82aecd24fe3181aa8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3963388a089da17755db`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ccc25bc7751c05d989d4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `abaa931de076aa1bcc5a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ad8ec4f8c7362e8b9a08`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2fe5afd13d3a5d0370b4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f4130e2fdd0688f6ebfc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f117db8694b15540843c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e872030b87e6f22a5d5e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `37d738413e78f319b392`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f0fa50ffb6dd150eb25c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `108324126af6f3751722`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7c570aec48c2b2af2303`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `063d39f3968092bdf5e4`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `1c2afa756a6f81bb2174`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `79263cb99d7a9eaac68f`
- Fields Used: _(None detected)_

**268b9361777451a42a01**

- Type: `None`
- Name: `268b9361777451a42a01`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c42326a3e7d6f193e6f9`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `0ff9e61d960d100dba8c`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `aa049c030e5a9cf7c0e0`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `a0044658c40aab9ffa6a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8cb03e680783605b03b2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `bbb9509eda04076550bb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3cf525a0b2148a00a2ab`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b0e9eaa164722f37ebd4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `075d886f06ca0142b119`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `440fae6f80de61117586`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `42f2bad1ae0ec28a42b7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `def0cd6efc79554f3a54`
- Fields Used: _(None detected)_

**barChart**

- Type: `barChart`
- Name: `50e9136c5cfb4a0d0f90`
- Fields Used:
  - `Average of DaysToClose` (Query: `Sum(Opportunities.DaysToClose)`) (Role: Y)
  - `Owner` (Query: `Owners.Owner`) (Role: Category)

**keyDriversVisual**

- Type: `keyDriversVisual`
- Name: `b760cae156950d9429f5`
- Fields Used:
  - `Territories.Territory` (Role: ExplainBy)
  - `Campaigns.Campaign Type` (Role: ExplainBy)
  - `Campaigns.Campaign` (Role: ExplainBy)
  - `Industries.Industry` (Role: ExplainBy)
  - `Opportunities.Purchase Process` (Role: ExplainBy)
  - `Owners.Owner` (Role: ExplainBy)
  - `Products.Product` (Role: ExplainBy)
  - `Opportunities.Decision Maker Identified` (Role: ExplainBy)
  - `Sum(Opportunities.Value)` (Role: ExplainBy)
  - `Territories.Region` (Role: ExplainBy)
  - `Owners.Manager` (Role: ExplainBy)
  - `Opportunities.DaysToClose` (Role: Target)
- Visual Level Filters:
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `0b171fbb8e7cff5f903b`
- Fields Used: _(None detected)_

**5a182e590787407ff806**

- Type: `None`
- Name: `5a182e590787407ff806`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e22d8d1046b3d73945da`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6f83dd34b2bd74299897`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ab8b2f68a2ff2868eab2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2a056dd34f7bd9e18a22`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e9681a75c3377891eec6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `65a30f5c2fc6026ce09b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `bf5a36711fa34922a399`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `74ce63ea215ce37f730a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4cba0e9b52ec536a0ef2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7fcfc6b35e4cef4c5a2f`
- Fields Used: _(None detected)_

**barChart**

- Type: `barChart`
- Name: `effa4d8ac53956038574`
- Fields Used:
  - `Average of DaysToClose` (Query: `Sum(Opportunities.DaysToClose)`) (Role: Y)
  - `Industry` (Query: `Industries.Industry`) (Role: Category)

**actionButton**

- Type: `actionButton`
- Name: `e954bb0e2c56c5dbeabc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `072e11a281e45b215ca7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f144076440cdcec8f3e5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e53c1aa76a50b049856b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8a806043692871813231`
- Fields Used: _(None detected)_

#### <a name="page-industries-overview"></a>Page: Industries Overview

*Internal Name: `ReportSection0e05747ca87ed9d14526`, Ordinal: 2*

##### Page Level Filters

- Filter on (Name: `Filter4`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter1`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter3`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter2`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter58495c8a81970d2c2350`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filterf6f8d6a01705e4bca438`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter7a44778ef49925c8f4c8`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter3b4bf36d9752d81a3f16`) (Type: N/A, Definition: N/A)

##### Visuals on this Page

**actionButton**

- Type: `actionButton`
- Name: `67b743a30eb4a022cc40`
- Fields Used: _(None detected)_

**39ee217d1a3feec79d90**

- Type: `None`
- Name: `39ee217d1a3feec79d90`
- Fields Used: _(None detected)_

**952f79c232d6033955c6**

- Type: `None`
- Name: `952f79c232d6033955c6`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `63f8cd134d1b2c546e10`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `53b9a67fb93c5692e0c0`
- Fields Used: _(None detected)_

**image**

- Type: `image`
- Name: `25649a488729cedc5363`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ac62f676a07d29853d7d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e2fb139655e530359b2c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c45b604e457d3d1c3e10`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `18b726022b00c3b04a29`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fc1b1911699008a82ee8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b704bcf043dae960105c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ca449f093d8e0d3c7adb`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `2c2505a4ab12c00b51e5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `05c06f7b0b771de4b776`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0a39b584a70ce9c3258`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d6f5b768689034dc9ab9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e11dc87a5c1da705967e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fdd9d8931902ba52ae27`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `716242218670d90de44e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9b12fb7a4aa010d33a02`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a6b440c17ed6a5990e3d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f5111a3036e5dd01d41b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `12570bee86d7899035e8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `10b7ecd0dd4d0ab0628d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2e53e95db60c4791408b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cbe0c31e040d404ce165`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f30eaf60a2613daeadca`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fc2c817088b08c604364`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `50cc21af2263adc00174`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ae8e7bef9e69c430044a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f9b60ad25dd59b647401`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b5037f187db1920d0344`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c0d34fdfec56b4bd9040`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ab97766eaba10386c490`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `84a549b82ed0a72791cc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a5f089b902104bd53b7b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0e95e681d06d4cd6c381`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0282a0a7c510500063c9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1eb443d392c321593160`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1bba2b247d2e7d0bb948`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0dba8df4022750c13be`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e1df1862d08402d204e9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `05318827005c7840b1d8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `233a1b9a56b8804e7e8e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b727dc9ed6772d0e0a8e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1ffc8b819211899a6664`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `96b0564492d200096461`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `5eb8c7376d5575276ab9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `26430087360535b618ed`
- Fields Used: _(None detected)_

**a3aa481aa5b5b10dd30a**

- Type: `None`
- Name: `a3aa481aa5b5b10dd30a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `345084ad874aa859652e`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `39b381f7ff73ea2f9384`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `dba1bbcce491ed77906b`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `31c6d22ae72ea9c9090d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5d1dd94705fa1d597d7e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2284c6cd7844101dbcf3`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f99e3d80380d6d2ee97a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1d2b32e2e6e245e25394`
- Fields Used: _(None detected)_

**scatterChart**

- Type: `scatterChart`
- Name: `91d4aae6951b9a7f20d2`
- Fields Used:
  - `Opportunity Count` (Query: `Opportunities.Opportunity Count`) (Role: Y)
  - `YEAR MONTH` (Query: `Opportunity Calendar.YEAR MONTH`) (Role: Play)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: X)
  - `Industry` (Query: `Industries.Industry`) (Role: Series)
  - `Revenue Won Average Deal Size` (Query: `Opportunities.Revenue Won Average Deal Size`) (Role: Size)
- Visual Level Filters:
  - Filter on (Name: `Filter799aec4798fb75202573`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filterd01d8eb8a807abf03efd`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter05535c7b85d34d3dead2`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter0896a65333b9569f4a80`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter458925e49dd909f18d13`) (Type: N/A, Definition: N/A)

**Sales by Industry**

- Type: `pivotTable`
- Name: `814eb9c828cad0453fa9`
- Fields Used:
  - `Industry` (Query: `Industries.Industry`) (Role: Rows)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Values)
  - `Close %` (Query: `Opportunities.Close %`) (Role: Values)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Values)
  - `Avg Win` (Query: `Opportunities.Revenue Won Average Deal Size`) (Role: Values)
- Visual Level Filters:
  - Filter on (Name: `Filterde1d162a090e2c24235a`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filtere51599c688bb1fb5ee41`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filtera1d136847cd4c34f2765`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter3b10123c85a51229eec8`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filtere373a227552edbe359d0`) (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `90d6c122090c45844405`
- Fields Used: _(None detected)_

**0350598d17066b8e4060**

- Type: `None`
- Name: `0350598d17066b8e4060`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a246f17b1ab3c41c6414`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5f217d9743cb79b02a77`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `43250fc10b7a2e201ce2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8b0070cd050c48bce7cb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0d5db2c7c903a7ca9aa7`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `f7842f99d3c628076f33`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1ebceb3e55379e0b5493`
- Fields Used: _(None detected)_

**Top Accounts**

- Type: `tableEx`
- Name: `495e2399c7bafb927dc5`
- Fields Used:
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Values)
  - `In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Values)
  - `Manager` (Query: `Owners.Manager`) (Role: Values)
  - `Owner` (Query: `Owners.Owner`) (Role: Values)
  - `Account Name` (Query: `Accounts.Account Name`) (Role: Values)

**actionButton**

- Type: `actionButton`
- Name: `d1c03f8ddc9cb006bb4a`
- Fields Used: _(None detected)_

**Revenue and forecast by Product**

- Type: `pivotTable`
- Name: `9f70be51c71a0fb66724`
- Fields Used:
  - `Products.Product LOB` (Role: Rows)
  - `Products.Product` (Role: Rows)
  - `Opportunities.Revenue Won` (Role: Values)
  - `Qualified Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Values)
  - `Opportunities.Forecast %` (Role: Values)

**actionButton**

- Type: `actionButton`
- Name: `b9eac3f38aebdc64b1d9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `41c2d1b9175094a0e5a6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ca0451cee1c762d244b7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4e037b92b7d80b1bdd90`
- Fields Used: _(None detected)_

**lineChart**

- Type: `lineChart`
- Name: `6a4271d1e93dedbcb59e`
- Fields Used:
  - `YEAR MONTH` (Query: `Opportunity Calendar.YEAR MONTH`) (Role: Category)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Y)
- Visual Level Filters:
  - Filter on (Name: `Filter799aec4798fb75202573`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter0896a65333b9569f4a80`) (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `97ba045dcd8175880064`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `af653d89aaecee28245c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `36ad89da8c179d89030d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1b5ded2e2843c002ddbc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5695a808844203c59645`
- Fields Used: _(None detected)_

#### <a name="page-pipeline-trends"></a>Page: Pipeline Trends

*Internal Name: `ReportSection9cc1f1d2d4c5bad9d959`, Ordinal: 3*

##### Page Level Filters

- Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter2`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter1`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filtere27aed5a6c11e1810292`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter7bb50368ad02e960c066`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter4c7edf308ee7ad495725`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter066acb2c76575ca537d8`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter171e438d51c3e0b3abd3`) (Type: N/A, Definition: N/A)

##### Visuals on this Page

**3bc326ae1d07c9debb8f**

- Type: `None`
- Name: `3bc326ae1d07c9debb8f`
- Fields Used: _(None detected)_

**53e109e7a6f50fc48f53**

- Type: `None`
- Name: `53e109e7a6f50fc48f53`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `997a7a8c70cc033d72c5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `17fabc43e4c79ca7a067`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1d9ed7c15fc0d8d1c268`
- Fields Used: _(None detected)_

**image**

- Type: `image`
- Name: `265d86b9a0339758c2e4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b85a8e3969e66a5ae037`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b7c0337539df863ee70b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6d6fe3a7302881fae2dc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7fc616472dd0cc68fe0e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `178e057c69f25ed1adbe`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c79b4732e758e266e371`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9fdd8b245a838b6d1199`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `f4c0d15b9af6f8e6f516`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0aaad21881ff1c3b68e9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f9dff087cae4b693f531`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `70b580062a3dd93fa779`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4a7cb9dea07a68a3db2c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4165d90d45aa767b4231`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b85c18fd5db45aadcf5a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5bc45eaffedfb37e2ac4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `23ba5d0e9c2f61ca1342`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c5c6e79bde34fa98a24c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `86bcffc3b23deb80cd13`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4538688bf22638df88fa`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1a3da1746f30fb281620`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `56ee325195103c2b5b96`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `33b17546d20dc52700c1`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `943a095aa0f1473d2102`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f15242559aab3f09e251`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1afbc81e47fe19d42b07`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6bfbc55a980baca7f8f5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5ef83ba64e1b3da6aaea`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d125f7b89b44e535c9f7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8c7db705c36891177cca`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ab8da6626e989f873b48`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7bf5d14746e96b6cab1b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5b295b0dc9117206cbef`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1b56b8549a4d26590032`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4f7f8dbe7b9eeed6faab`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `003a42bf63ffcaeec511`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `efae7e36058c53407737`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9016697b746e67486f70`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f2869c90e3018089ecfa`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3bebe7ef27f0238bb29c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `30d70d4b95ff37e599ed`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3b2e7f76a88e60b251d5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `bb16058fc398f7658f6e`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `242cf72542dd7f870913`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4f77cda20566e80e78c1`
- Fields Used: _(None detected)_

**92d973cb41b6ce96bfbf**

- Type: `None`
- Name: `92d973cb41b6ce96bfbf`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f4157efd984fc0290711`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `a97676829e5f17adf5d7`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `b4cdd8cd9b643e95efe1`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `f5e6bab28420078a07e0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1847b81fcbad09500c39`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fdf514bbfcb8ca4f0ce5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8edb09250579ec3c33b6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b53477ddaa241dc6d885`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `667ac8099951eee864b8`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `d6f0ee03200eb6271ffb`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `521c6226b786b50a090c`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `a1a3cab5f9bd0725c32c`
- Fields Used: _(None detected)_

**Total Pipeline**

- Type: `kpi`
- Name: `afe40545919fea1c21e2`
- Fields Used:
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)
  - `Revenue Open` (Query: `Opportunities.Revenue Open`) (Role: Indicator)

**Avg Days Remaining**

- Type: `kpi`
- Name: `5d53dc3013109227fc0b`
- Fields Used:
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)
  - `Days Remaining In Pipeline` (Query: `Avg(Opportunities.Days Remaining In Pipeline)`) (Role: Indicator)

**Qualified Pipeline**

- Type: `kpi`
- Name: `281c319c6d38c8f24097`
- Fields Used:
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Indicator)

**Opportunity Count**

- Type: `kpi`
- Name: `5354ed80d85d6ad0ca02`
- Fields Used:
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)
  - `Opportunity Count` (Query: `Opportunities.Opportunity Count`) (Role: Indicator)

**actionButton**

- Type: `actionButton`
- Name: `2b6aa218a2e41c68463e`
- Fields Used: _(None detected)_

**a0ac1ff97e4b6be2eda3**

- Type: `None`
- Name: `a0ac1ff97e4b6be2eda3`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `930de974db7d81a7cc91`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `0f043dcff185530810ab`
- Fields Used: _(None detected)_

**Revenue Open by Product Category and Territory**

- Type: `barChart`
- Name: `818a83bb2ae23dd1ec20`
- Fields Used:
  - `Product Category` (Query: `Products.Product LOB`) (Role: Category)
  - `Product` (Query: `Products.Product`) (Role: Category)
  - `Revenue Open` (Query: `Opportunities.Revenue Open`) (Role: Y)
  - `Territory` (Query: `Territories.Territory`) (Role: Rows)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Tooltips)
  - `Opportunity Count In Pipeline` (Query: `Opportunities.Opportunity Count In Pipeline`) (Role: Tooltips)
- Visual Level Filters:
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)

**Pipeline by Top Industries**

- Type: `ribbonChart`
- Name: `6fe682ad2620c1cefca0`
- Fields Used:
  - `YEAR MONTH` (Query: `Opportunity Calendar.YEAR MONTH`) (Role: Category)
  - `Revenue Open` (Query: `Opportunities.Revenue Open`) (Role: Y)
  - `Industry` (Query: `Industries.Industry`) (Role: Series)
- Visual Level Filters:
  - Filter on (Name: `Filterde1d162a090e2c24235a`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filtere51599c688bb1fb5ee41`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filterb7101e64d7144f00fcb0`) (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `e507075273fd92e7a647`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3226d26ce9b3840701b0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9018a024f6284744065a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e7d1b041eb8c15e309ef`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `79e038208022792f320b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `01a1079348f3a8f8da65`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `80213dbd27f3d64abd2d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8e2030d5e4f29a9795ac`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0c51b0a51727934a561`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ee92f833bf653c4ae894`
- Fields Used: _(None detected)_

**tableEx**

- Type: `tableEx`
- Name: `179c06ea397a8a000d0b`
- Fields Used:
  - `Account Name` (Query: `Accounts.Account Name`) (Role: Values)
  - `Owner` (Query: `Owners.Owner`) (Role: Values)
  - `Product` (Query: `Products.Product`) (Role: Values)
  - `Value` (Query: `Sum(Opportunities.Value)`) (Role: Values)
  - `Discount` (Query: `Avg(Opportunities.Discount)`) (Role: Values)
  - `Sales Stage` (Query: `Opportunities.PipelineStep`) (Role: Values)
  - `Rating` (Query: `Opportunities.Rating`) (Role: Values)
  - `Weeks Open` (Query: `Sum(Opportunities.Weeks Open)`) (Role: Values)
  - `Days Until Close` (Query: `Avg(Opportunities.Days Remaining In Pipeline)`) (Role: Values)
  - `Territory` (Query: `Territories.Territory`) (Role: Values)
  - `Industry` (Query: `Industries.Industry`) (Role: Values)

**actionButton**

- Type: `actionButton`
- Name: `98507be1b8d269dcf901`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `bc7885962ece6e8fb48f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5a55427ad115437d5146`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d753b8aaf90455e30085`
- Fields Used: _(None detected)_

#### <a name="page-qa-query"></a>Page: Q&A Query

*Internal Name: `ReportSectione4490b0fc1862a3c9b5a`, Ordinal: 9*

##### Page Level Filters

- Filter on (Name: `Filter7`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter8`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter5`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter3`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter4`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter2`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter1`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter6`) (Type: N/A, Definition: N/A)

##### Visuals on this Page

**8c484f2f40452c7cf191**

- Type: `None`
- Name: `8c484f2f40452c7cf191`
- Fields Used: _(None detected)_

**21587fd7bcc0f4a2f142**

- Type: `None`
- Name: `21587fd7bcc0f4a2f142`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `0dd68c3feec184f20d8d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4f4ea07a1fd42bb2a04e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `44ac085ba849dd9432cb`
- Fields Used: _(None detected)_

**image**

- Type: `image`
- Name: `f71c71e2fd376bad9855`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `09b40f559fe9b1819f18`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `955a13335c4566d0e924`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `930ec9509e6056568802`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cd78f85486e435c36358`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b3b7f49ebabdb194f78f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e48283be721b409d53f2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9c9dd31de24c5e822e56`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `41536f27aae4e16d9a51`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c6b7f52b836257b66a52`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `dc437c0702bd485d5b75`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4cc0fd2edcd0eab76a04`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c1d626c878344d227f9d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `acbe85ff55504b4b3e0a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `afeb5790db55634d480d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `69b6b266b0e8c8453199`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d2e09a3d75557fd26a1d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d0d73d8faf9aa7025ac5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3217066c939c7789754a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `bd63f2f03ec0f4d554ae`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c875771655152ba3e01e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a7cd66f38059f561bc48`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d7d8d1147065021c3db5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8c27bdf8df05193a0d87`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5031d2cdab826ca852f4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `891440710f5a3bce4575`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3249c139cd202fd0fbb7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8ab09c945c814bf8f4bb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4e275d35f0eb0b2b9e88`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0dfa5d746b3a584648e6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `089809c1254e4ecc1333`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `10df7c862ee6b71f3c22`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `08d2b258bb844da491f8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2967205e76c4615f24c8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d09a82b76eaa27fc3b77`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `695460970c2ce3d76ca6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cb37a8038c33b871a875`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4b732c3396cd634981fb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7398016ae45731d37cf1`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e9ddbe5ab732151f14d0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `21252cf0da3a8e6d346e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ab3be1c67244a90c4c6c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1f69eb3fcb445ca6fa4d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f88a9b25c10b31254d02`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `62203b34deb27a63327e`
- Fields Used: _(None detected)_

**3385aea9820dedc06340**

- Type: `None`
- Name: `3385aea9820dedc06340`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ddaef79149243fe37401`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `82d7da09a3de86b1cff2`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `6aa47ee5372fc753a40e`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `7e1618a0aa1e97ffffcc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8e8eea02bf33edab4167`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `50f0d55e70579fd8f125`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3251d5a4b0e982c8c0aa`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fb61a760920c0dbf24f1`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c99c64557510b88d9a13`
- Fields Used: _(None detected)_

**qnaVisual**

- Type: `qnaVisual`
- Name: `954d6f9432c76cbb2ca1`
- Fields Used:
  - `Accounts.Industry` (Role: ExplainBy)
  - `Owners.Owner` (Role: ExplainBy)
  - `Products.Product` (Role: ExplainBy)
  - `Accounts.Territory` (Role: ExplainBy)
  - `Accounts.Region` (Role: ExplainBy)
  - `Products.Product LOB` (Role: ExplainBy)
  - `Owners.Manager` (Role: ExplainBy)
  - `Opportunities.Discount` (Role: Target)

**actionButton**

- Type: `actionButton`
- Name: `e0cdb5f878049e3e4ed9`
- Fields Used: _(None detected)_

**b8af85efb20c2bd7a654**

- Type: `None`
- Name: `b8af85efb20c2bd7a654`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `10daff11ecb34787bae4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ee576d05beece2efe815`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `94bac5bf7f77ce338654`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `37181c7f40c6b675093a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1724f4f22445f39678b7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `36e079c981e4c2014ca5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e5ad97c9251051ea8615`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9a7dd40cab7d77c8aa4f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `bcd844492cb53aca397c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f30d1849b842297726c0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e5a0ca99f097eacc47d2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3c6b36e8bdeb96445bff`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e6bf05e47d6624fd0157`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a1de1745bf7a2f8d9efe`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `77ffc26105838020dfa7`
- Fields Used: _(None detected)_

#### <a name="page-revenue-source-breakdown"></a>Page: Revenue Source Breakdown

*Internal Name: `ReportSectionacd41c847407a998c130`, Ordinal: 8*

##### Page Level Filters

- Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter7`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter8`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter5`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter3`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter4`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter2`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter1`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter6`) (Type: N/A, Definition: N/A)

##### Visuals on this Page

**cb0cc9f15187bcd69a2d**

- Type: `None`
- Name: `cb0cc9f15187bcd69a2d`
- Fields Used: _(None detected)_

**16c33421cba4471a02a9**

- Type: `None`
- Name: `16c33421cba4471a02a9`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `2bafa035b14767f73c2c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f0aeb47a8ac7599f9c31`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0277ce59071fb8c9f626`
- Fields Used: _(None detected)_

**image**

- Type: `image`
- Name: `072b2f3f554830a32b88`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1722e13107d69c6a9874`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `437ec05e27652c5c860f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7bba1aa302de3c17859a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7d0b13dfbc6174e8440c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d16e01900cd4feaf36de`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `83f1ea560603469f29c2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c5d86482a399da943e88`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `464c1811966871342005`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `beb2f2d34362c7682ed2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `36b2c1a20c2ec06715e2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `700f547ef3d96c8f0406`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7d1a27bf99761e845702`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5de554f86ed5ce21dcee`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2dd46234ec261cbc6b4e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b2eaa58e860bdc9933d0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `14f52053b6dfe4510229`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0ad6c17a73f1fca53ee2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c477d3fa5c1b7c931be6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `507a57e0795e0484538b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `250bb1028741537976e1`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0f374e5439732eed951`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `caf487a2d37e388372c2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c39a347ffe9310311418`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `26e994bee5d453fb52ce`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `39eaa03c598d603504f5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `72da29a113d7edd203a3`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b1b7adf388b0864c9656`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f61808b53ae0c9442bf8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6f0211613c75ec06df16`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a538b889988ddcafb0b0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7519e9dd480b9fc81c7c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cb5b2d5761a95828c0d5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6c0daac7aaadcf8f4d73`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `953fb35f7bfa5dc2a4bb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7a059b87b8f9c577c0c0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0e29d58bfa44ab2c7b5e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6fd642e62022a6d30583`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d27e40f92268f0ca3056`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `472dbff67e2bbc7d76f7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `120c4ad3c4f06d438301`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c9a3d54ed3324c64c94f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e2f7e059a98ec18bed8e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `90ba2a5f682892b274ce`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `ad176f220b8601d3b8f2`
- Fields Used: _(None detected)_

**4a5ae72df61c80de4675**

- Type: `None`
- Name: `4a5ae72df61c80de4675`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f039f96c7690d0f77c25`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `c3a8e402fe466a1c2140`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `65d61a0c3c2edff30eae`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `b894c962963699d05a92`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6ab1ce140264c8a1887d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `87fbe49266122217bc47`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9cc18bd577731f222839`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `39b2e2fe480ebd25061e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `65fc8de38577ef9c7793`
- Fields Used: _(None detected)_

**decompositionTreeVisual**

- Type: `decompositionTreeVisual`
- Name: `954d6f9432c76cbb2ca1`
- Fields Used:
  - `Product` (Query: `Products.Product`) (Role: ExplainBy)
  - `Product Category` (Query: `Products.Product LOB`) (Role: ExplainBy)
  - `Value` (Query: `Sum(Opportunities.Value)`) (Role: Analyze)
  - `Industry` (Query: `Industries.Industry`) (Role: ExplainBy)
  - `Territory` (Query: `Territories.Territory`) (Role: ExplainBy)
  - `Owner` (Query: `Owners.Owner`) (Role: ExplainBy)
  - `Campaign` (Query: `Campaigns.Campaign`) (Role: ExplainBy)
- Visual Level Filters:
  - Filter on (Name: `Filter9eafa29b773622144b40`) (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `15628057775d6154adb7`
- Fields Used: _(None detected)_

**5480d15dcdfe99da58ad**

- Type: `None`
- Name: `5480d15dcdfe99da58ad`
- Fields Used: _(None detected)_

**barChart**

- Type: `barChart`
- Name: `24a67f1afa332056d39b`
- Fields Used:
  - `Opportunity Count` (Query: `Opportunities.Opportunity Count`) (Role: Y)
  - `Territory` (Query: `Territories.Territory`) (Role: Category)

**actionButton**

- Type: `actionButton`
- Name: `fdae39816e83940c4bce`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ab97f7cf38a61bc29a71`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `68f95dedb09e090fbe54`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d135b6a8839d03982210`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `67e41e3acf317ce247a0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8055331ce605d29aafd6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e606aa8a457ebbeeafc8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `bc0c357aef24b7a12bef`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `96a18979010805d6491f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2466c309630fd9ccebd4`
- Fields Used: _(None detected)_

**barChart**

- Type: `barChart`
- Name: `143a9f40e6397414f4d5`
- Fields Used:
  - `Opportunity Count` (Query: `Opportunities.Opportunity Count`) (Role: Y)
  - `Owner` (Query: `Owners.Owner`) (Role: Category)
  - `Manager` (Query: `Owners.Manager`) (Role: Category)

**actionButton**

- Type: `actionButton`
- Name: `64fadadbe59602464a4b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f0d93785fed7466d3d51`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `acbe2d9929e5160a89e9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d206fcd8361721442aad`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3c53d19f70980e243db0`
- Fields Used: _(None detected)_

#### <a name="page-sales-discounting-insights"></a>Page: Sales Discounting Insights

*Internal Name: `ReportSection46edb4426e9aacd8d4b9`, Ordinal: 7*

##### Page Level Filters

- Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter7`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter8`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter5`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter3`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter4`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter2`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter1`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter6`) (Type: N/A, Definition: N/A)

##### Visuals on this Page

**57b4eb01882381d5af4f**

- Type: `None`
- Name: `57b4eb01882381d5af4f`
- Fields Used: _(None detected)_

**ca23ede55fd7e9d0e40b**

- Type: `None`
- Name: `ca23ede55fd7e9d0e40b`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `9fef4b07b67093c1af7e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a0c42b806a5dd3064174`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7255c26cef8d8ec4b969`
- Fields Used: _(None detected)_

**image**

- Type: `image`
- Name: `490ec9d3cadb96356def`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d8fea2aee7e919419faf`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b93fed68cd1c84d858d1`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7b65536a6838aeb06142`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b116ecedd9d4cd3a4f76`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a590338f671965b2b49b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `01a9a80baac7a14ea9a8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `060116e3bd022230530b`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `9fe58244e6ffc167c857`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0584f0c45c9b53dab2eb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d03c588bf3f4785b5392`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `796b54532f49d3866d38`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6c82111e81c4ee146e26`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `628ba01bb38f816da341`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `149429a046e3fd94e310`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d2733eb7a181b9ed8794`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `16008e7ea6623da991d8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `af89dd739a3c7b05ebec`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9e9a354943c735a99087`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `beeb134c2d5ac16243fb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c93f86b205ebab0e7654`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3a3f5d33eac89dad91c7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2d769c57c1a5ec559ed4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `01e9572b1cfdba53f828`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a1a85e7fc117e4e2f0bf`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `60a8ae844b76876342f5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `aef1842b5f2611945b04`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f4b6f347bfbf74388630`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `95e52b459ee3b6b7a5e9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e9caccc3730f44f2e0bd`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6926fce3bf498a417c7d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9fd56153246ce22d22b4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a91f3a94221bba4eb3f0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7050c0e75cb9cbfbd240`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `56382676e4f195569432`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4d9fbad909c54909867b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3cb62a7629595e70c765`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `53f5416e6a7e50b619fb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9309b09b614b343f51ef`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f96f3c3c4570ea15246f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f816878c761aa61f972f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fcb2f77f88e655ba8143`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `674e33c37058c5821c10`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `7fa0d8cd4837e2833ec5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d5ad7331b126d75f0e4a`
- Fields Used: _(None detected)_

**c75549bc09e67d2638fe**

- Type: `None`
- Name: `c75549bc09e67d2638fe`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0870b762e8df6442a9e`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `0b3db36ebc356c4d6fa5`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `6e6fa481fce4fd752330`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `6cb14e5d8c15b6e35ad9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7aab195c6dee366d99b3`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0b5aa3d8c980af72d39f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ef119ce72c905b230a4e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f17ce2e1e18c9cfc70a0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8e57d3c065d7006100a5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c0f1beb9500b82ae21d5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9d3838da6553e0644e41`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a1f21b7bd0a9ed498a95`
- Fields Used: _(None detected)_

**barChart**

- Type: `barChart`
- Name: `c5628ab58003046a7359`
- Fields Used:
  - `Discount` (Query: `Avg(Opportunities.Discount)`) (Role: Y)
  - `Territory` (Query: `Territories.Territory`) (Role: Category)

**keyDriversVisual**

- Type: `keyDriversVisual`
- Name: `a43b3de5dd491089d2b4`
- Fields Used:
  - `Products.Product` (Role: ExplainBy)
  - `Owners.Manager` (Role: ExplainBy)
  - `Owners.Owner` (Role: ExplainBy)
  - `Products.Product LOB` (Role: ExplainBy)
  - `Industries.Industry` (Role: ExplainBy)
  - `Campaigns.Campaign` (Role: ExplainBy)
  - `Campaigns.Campaign Type` (Role: ExplainBy)
  - `Territories.Region` (Role: ExplainBy)
  - `Territories.Territory` (Role: ExplainBy)
  - `Opportunities.Discount` (Role: Target)
- Visual Level Filters:
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `ca62d4a65f582000e58e`
- Fields Used: _(None detected)_

**3fcd8179d701269d9066**

- Type: `None`
- Name: `3fcd8179d701269d9066`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `be64b1cd7d038bf0a2ae`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `eccdb680581d5a78eb23`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8fb86e79337eb35d34e6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0ae3f532358fcabd518a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d36b1d78a86f19636562`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5ba760b4a075f6e1c84c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2f09feecedb17a948157`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3b75aa1a84747a02d029`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f0f4c153b9ab9c484b1b`
- Fields Used: _(None detected)_

**Discount by Manager/Owner**

- Type: `barChart`
- Name: `3388fa4da1c0278c0009`
- Fields Used:
  - `Discount` (Query: `Avg(Opportunities.Discount)`) (Role: Y)
  - `Owner` (Query: `Owners.Owner`) (Role: Category)
  - `Manager` (Query: `Owners.Manager`) (Role: Category)

**actionButton**

- Type: `actionButton`
- Name: `f6a50284af9194ef331a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9fcdd88fd43736784ca4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b213df32b3a44c58e2a9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `27d3d03c23a7156b3368`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `50cee176c58b7bba0ddb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `11da79ceecd9cf643411`
- Fields Used: _(None detected)_

#### <a name="page-sales-overview"></a>Page: Sales Overview

*Internal Name: `ReportSectionb621f12070647be09138`, Ordinal: 0*

##### Page Level Filters

- Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter4`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter1`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter3`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter2`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter58495c8a81970d2c2350`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filterf6f8d6a01705e4bca438`) (Type: N/A, Definition: N/A)

##### Visuals on this Page

**actionButton**

- Type: `actionButton`
- Name: `67b743a30eb4a022cc40`
- Fields Used: _(None detected)_

**39ee217d1a3feec79d90**

- Type: `None`
- Name: `39ee217d1a3feec79d90`
- Fields Used: _(None detected)_

**952f79c232d6033955c6**

- Type: `None`
- Name: `952f79c232d6033955c6`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `63f8cd134d1b2c546e10`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `53b9a67fb93c5692e0c0`
- Fields Used: _(None detected)_

**image**

- Type: `image`
- Name: `25649a488729cedc5363`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ac62f676a07d29853d7d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e2fb139655e530359b2c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c45b604e457d3d1c3e10`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `18b726022b00c3b04a29`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fc1b1911699008a82ee8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b704bcf043dae960105c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ca449f093d8e0d3c7adb`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `2c2505a4ab12c00b51e5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `05c06f7b0b771de4b776`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0a39b584a70ce9c3258`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d6f5b768689034dc9ab9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e11dc87a5c1da705967e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fdd9d8931902ba52ae27`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `716242218670d90de44e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9b12fb7a4aa010d33a02`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a6b440c17ed6a5990e3d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f5111a3036e5dd01d41b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `12570bee86d7899035e8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `10b7ecd0dd4d0ab0628d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2e53e95db60c4791408b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cbe0c31e040d404ce165`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f30eaf60a2613daeadca`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fc2c817088b08c604364`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `50cc21af2263adc00174`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ae8e7bef9e69c430044a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f9b60ad25dd59b647401`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b5037f187db1920d0344`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c0d34fdfec56b4bd9040`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ab97766eaba10386c490`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `84a549b82ed0a72791cc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a5f089b902104bd53b7b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0e95e681d06d4cd6c381`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0282a0a7c510500063c9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1eb443d392c321593160`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1bba2b247d2e7d0bb948`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0dba8df4022750c13be`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e1df1862d08402d204e9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `05318827005c7840b1d8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `233a1b9a56b8804e7e8e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b727dc9ed6772d0e0a8e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1ffc8b819211899a6664`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `96b0564492d200096461`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `5eb8c7376d5575276ab9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `26430087360535b618ed`
- Fields Used: _(None detected)_

**a3aa481aa5b5b10dd30a**

- Type: `None`
- Name: `a3aa481aa5b5b10dd30a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `345084ad874aa859652e`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `39b381f7ff73ea2f9384`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `dba1bbcce491ed77906b`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `31c6d22ae72ea9c9090d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c0f64f688adaf310d1cc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `283a163f881a5b79ecf3`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `74d0ffafc459f0161b99`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1d2b32e2e6e245e25394`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `f41f2f87b47b937e76b8`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `0d27dd0157a15a1ab3c2`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `95f8915b7879ee034570`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `f07d80835a665c2499b9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `90d6c122090c45844405`
- Fields Used: _(None detected)_

**Qualified Pipeline**

- Type: `kpi`
- Name: `c5c8a883a7a48a40a5eb`
- Fields Used:
  - `Qualified Rev In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Indicator)
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)

**Revenue goal**

- Type: `kpi`
- Name: `9076cf822e52a295ac32`
- Fields Used:
  - `Rev Goal` (Query: `Owners.Rev Goal`) (Role: Indicator)
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)

**Forecast**

- Type: `kpi`
- Name: `8a0ce2360f3fa1944ab8`
- Fields Used:
  - `Forecast %` (Query: `Opportunities.Forecast %`) (Role: Indicator)
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)

**Revenue won**

- Type: `kpi`
- Name: `18ee1fa1b11e72e1895a`
- Fields Used:
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Indicator)
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)

**0350598d17066b8e4060**

- Type: `None`
- Name: `0350598d17066b8e4060`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a246f17b1ab3c41c6414`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5f217d9743cb79b02a77`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `21079dbce2c0c94ddab3`
- Fields Used: _(None detected)_

**slicer**

- Type: `slicer`
- Name: `f4ef9aeaa37645adde86`
- Fields Used:
  - `Forecast Adjustment` (Query: `Forecast Adjustment.Forecast Adjustment`) (Role: Values)
  - `Fcst adj slicer alt text` (Query: `Opportunity Forecast Adjustment.Fcst adj slicer alt text`) (Role: Unknown)

**funnel**

- Type: `funnel`
- Name: `f37cb3116b6b7130b995`
- Fields Used:
  - `Sales Stage` (Query: `Opportunities.PipelineStep`) (Role: Category)
  - `Revenue Open` (Query: `Opportunities.Revenue Open`) (Role: Y)
- Visual Level Filters:
  - Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)

**Revenue Won and Revenue In Pipeline by Product LOB**

- Type: `barChart`
- Name: `90b98cca54dd8f762bb3`
- Fields Used:
  - `Product Category` (Query: `Products.Product LOB`) (Role: Category)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Y)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Y)
  - `Product` (Query: `Products.Product`) (Role: Category)
- Visual Level Filters:
  - Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `43250fc10b7a2e201ce2`
- Fields Used: _(None detected)_

**columnChart**

- Type: `columnChart`
- Name: `9977560f84a487275f20`
- Fields Used:
  - `Forecast Adjustment` (Query: `Opportunity Forecast Adjustment.Forecast Adjustment`) (Role: Category)
  - `Blank` (Query: `Sum(Opportunity Forecast Adjustment.Blank)`) (Role: Y)

**actionButton**

- Type: `actionButton`
- Name: `8b0070cd050c48bce7cb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0d5db2c7c903a7ca9aa7`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `f7842f99d3c628076f33`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `9efd5153059fc12dcb3f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1ebceb3e55379e0b5493`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4fb5f1e871be0d238563`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4c3cd177079b0ac4c639`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d1c03f8ddc9cb006bb4a`
- Fields Used: _(None detected)_

**(Right click to drill to Users)**

- Type: `lineStackedColumnComboChart`
- Name: `5245dfb1a52da9fcc8c4`
- Fields Used:
  - `Owners.Manager` (Role: Category)
  - `Owners.Owner` (Role: Category)
  - `Revenue won` (Query: `Opportunities.Revenue Won`) (Role: Y)
  - `Qualified pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Y)
  - `Goal` (Query: `Owners.Owner Goal`) (Role: Y2)
  - `Qualified pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Tooltips)
  - `Revenue won` (Query: `Opportunities.Revenue Won`) (Role: Tooltips)
- Visual Level Filters:
  - Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)

**Revenue and forecast by Product**

- Type: `pivotTable`
- Name: `9f70be51c71a0fb66724`
- Fields Used:
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Values)
  - `Qualified Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Values)
  - `Forecast %` (Query: `Opportunities.Forecast %`) (Role: Values)
  - `Product Category` (Query: `Products.Product LOB`) (Role: Rows)
  - `Product` (Query: `Products.Product`) (Role: Rows)

**actionButton**

- Type: `actionButton`
- Name: `b9eac3f38aebdc64b1d9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `41c2d1b9175094a0e5a6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ca0451cee1c762d244b7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4e037b92b7d80b1bdd90`
- Fields Used: _(None detected)_

**Forecast by Territory**

- Type: `pivotTable`
- Name: `e9ee7b2d33b6ec76638d`
- Fields Used:
  - `In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Values)
  - `Forecast %` (Query: `Opportunities.Forecast %`) (Role: Values)
  - `Territory` (Query: `Territories.Territory`) (Role: Rows)
  - `State or Province` (Query: `Accounts.State or Province`) (Role: Rows)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Values)

**shapeMap**

- Type: `shapeMap`
- Name: `db4e5eed33a1f6bec037`
- Fields Used:
  - `State or Province` (Query: `Accounts.Street Hierarchy.State or Province`) (Role: Category)
  - `State or Province` (Query: `Min(Accounts.Street Hierarchy.State or Province)`) (Role: Tooltips)
  - `Rev Goal` (Query: `Owners.Rev Goal`) (Role: Tooltips)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Tooltips)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Tooltips)

**actionButton**

- Type: `actionButton`
- Name: `97ba045dcd8175880064`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `af653d89aaecee28245c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `36ad89da8c179d89030d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1b5ded2e2843c002ddbc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5695a808844203c59645`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `0d5e7415771adabfa871`
- Fields Used: _(None detected)_

#### <a name="page-template"></a>Page: Template

*Internal Name: `ReportSection7813318f563ba25c9399`, Ordinal: 10*

##### Page Level Filters

- Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter4`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter1`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter3`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter2`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter58495c8a81970d2c2350`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filterf6f8d6a01705e4bca438`) (Type: N/A, Definition: N/A)

##### Visuals on this Page

**39ee217d1a3feec79d90**

- Type: `None`
- Name: `39ee217d1a3feec79d90`
- Fields Used: _(None detected)_

**952f79c232d6033955c6**

- Type: `None`
- Name: `952f79c232d6033955c6`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `63f8cd134d1b2c546e10`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `53b9a67fb93c5692e0c0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `67b743a30eb4a022cc40`
- Fields Used: _(None detected)_

**image**

- Type: `image`
- Name: `25649a488729cedc5363`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ac62f676a07d29853d7d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e2fb139655e530359b2c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c45b604e457d3d1c3e10`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `18b726022b00c3b04a29`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fc1b1911699008a82ee8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b704bcf043dae960105c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ca449f093d8e0d3c7adb`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `2c2505a4ab12c00b51e5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `05c06f7b0b771de4b776`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0a39b584a70ce9c3258`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d6f5b768689034dc9ab9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e11dc87a5c1da705967e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fdd9d8931902ba52ae27`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `716242218670d90de44e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9b12fb7a4aa010d33a02`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a6b440c17ed6a5990e3d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f5111a3036e5dd01d41b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `12570bee86d7899035e8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `10b7ecd0dd4d0ab0628d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2e53e95db60c4791408b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cbe0c31e040d404ce165`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f30eaf60a2613daeadca`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fc2c817088b08c604364`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `50cc21af2263adc00174`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ae8e7bef9e69c430044a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f9b60ad25dd59b647401`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b5037f187db1920d0344`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c0d34fdfec56b4bd9040`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ab97766eaba10386c490`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `84a549b82ed0a72791cc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a5f089b902104bd53b7b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0e95e681d06d4cd6c381`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0282a0a7c510500063c9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1eb443d392c321593160`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1bba2b247d2e7d0bb948`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0dba8df4022750c13be`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e1df1862d08402d204e9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `05318827005c7840b1d8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `233a1b9a56b8804e7e8e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b727dc9ed6772d0e0a8e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `26430087360535b618ed`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `5eb8c7376d5575276ab9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1ffc8b819211899a6664`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `96b0564492d200096461`
- Fields Used: _(None detected)_

**a3aa481aa5b5b10dd30a**

- Type: `None`
- Name: `a3aa481aa5b5b10dd30a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `345084ad874aa859652e`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `39b381f7ff73ea2f9384`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `dba1bbcce491ed77906b`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `31c6d22ae72ea9c9090d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1d2b32e2e6e245e25394`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `90d6c122090c45844405`
- Fields Used: _(None detected)_

**0350598d17066b8e4060**

- Type: `None`
- Name: `0350598d17066b8e4060`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a246f17b1ab3c41c6414`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5f217d9743cb79b02a77`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `43250fc10b7a2e201ce2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8b0070cd050c48bce7cb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0d5db2c7c903a7ca9aa7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1ebceb3e55379e0b5493`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d1c03f8ddc9cb006bb4a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b9eac3f38aebdc64b1d9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `41c2d1b9175094a0e5a6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ca0451cee1c762d244b7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4e037b92b7d80b1bdd90`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `97ba045dcd8175880064`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `af653d89aaecee28245c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `36ad89da8c179d89030d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1b5ded2e2843c002ddbc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5695a808844203c59645`
- Fields Used: _(None detected)_

#### <a name="page-trend-analytics"></a>Page: Trend Analytics

*Internal Name: `ReportSection08507840a0c5d0d26f29`, Ordinal: 4*

##### Page Level Filters

- Filter on (Name: `Filter4`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter1`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter3`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter2`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter58495c8a81970d2c2350`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filterf6f8d6a01705e4bca438`) (Type: N/A, Definition: N/A)

##### Visuals on this Page

**39ee217d1a3feec79d90**

- Type: `None`
- Name: `39ee217d1a3feec79d90`
- Fields Used: _(None detected)_

**952f79c232d6033955c6**

- Type: `None`
- Name: `952f79c232d6033955c6`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `63f8cd134d1b2c546e10`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `53b9a67fb93c5692e0c0`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `6c1414c23d44039c8f9b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `67b743a30eb4a022cc40`
- Fields Used: _(None detected)_

**image**

- Type: `image`
- Name: `25649a488729cedc5363`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ac62f676a07d29853d7d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e2fb139655e530359b2c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c45b604e457d3d1c3e10`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `18b726022b00c3b04a29`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fc1b1911699008a82ee8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b704bcf043dae960105c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ca449f093d8e0d3c7adb`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `2c2505a4ab12c00b51e5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `05c06f7b0b771de4b776`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0a39b584a70ce9c3258`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d6f5b768689034dc9ab9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e11dc87a5c1da705967e`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `63920b163aafcd295561`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `bd53cfa73af33d39e8de`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fdd9d8931902ba52ae27`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `716242218670d90de44e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9b12fb7a4aa010d33a02`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a6b440c17ed6a5990e3d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f5111a3036e5dd01d41b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `12570bee86d7899035e8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `10b7ecd0dd4d0ab0628d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2e53e95db60c4791408b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cbe0c31e040d404ce165`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f30eaf60a2613daeadca`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `92a1ddc5a1653982f6b0`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `95ed50764c9f06852a55`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fc2c817088b08c604364`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `50cc21af2263adc00174`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ae8e7bef9e69c430044a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f9b60ad25dd59b647401`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b5037f187db1920d0344`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c0d34fdfec56b4bd9040`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ab97766eaba10386c490`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `84a549b82ed0a72791cc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a5f089b902104bd53b7b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0e95e681d06d4cd6c381`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0282a0a7c510500063c9`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `98afeb6ebbecdadae244`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `01f280c9494b8b8cb9e0`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1eb443d392c321593160`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1bba2b247d2e7d0bb948`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0dba8df4022750c13be`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e1df1862d08402d204e9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `05318827005c7840b1d8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `233a1b9a56b8804e7e8e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b727dc9ed6772d0e0a8e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1ffc8b819211899a6664`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `96b0564492d200096461`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `5eb8c7376d5575276ab9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `26430087360535b618ed`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `58b5d3eae37a63ef52bd`
- Fields Used: _(None detected)_

**a3aa481aa5b5b10dd30a**

- Type: `None`
- Name: `a3aa481aa5b5b10dd30a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `345084ad874aa859652e`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `39b381f7ff73ea2f9384`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `dba1bbcce491ed77906b`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `31c6d22ae72ea9c9090d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c6c8d59df473b47d3a4d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e4bc33c2cd8040a434f7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1d2b32e2e6e245e25394`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `90d6c122090c45844405`
- Fields Used: _(None detected)_

**8aac85e22fe8529c89e9**

- Type: `None`
- Name: `8aac85e22fe8529c89e9`
- Fields Used: _(None detected)_

**Won Opportunities this month**

- Type: `kpi`
- Name: `5530f4f73271531a70f9`
- Fields Used:
  - `Count of Won` (Query: `Opportunities.Count of Won`) (Role: Indicator)
  - `RELATIVE 30 DAY PERIOD` (Query: `Opportunity Calendar.RELATIVE 30 DAY PERIOD`) (Role: TrendLine)

**Close Ratio**

- Type: `kpi`
- Name: `ce82c03a8784cedd3490`
- Fields Used:
  - `Close %` (Query: `Opportunities.Close %`) (Role: Indicator)
  - `RELATIVE MONTH` (Query: `Opportunity Calendar.RELATIVE MONTH`) (Role: TrendLine)

**Avg Discount**

- Type: `kpi`
- Name: `973d34f6bdc02e3a4e72`
- Fields Used:
  - `Discount` (Query: `Avg(Opportunities.Discount)`) (Role: Indicator)
  - `RELATIVE MONTH` (Query: `Opportunity Calendar.RELATIVE MONTH`) (Role: TrendLine)
- Visual Level Filters:
  - Filter on Unknown Target (Type: N/A, Definition: N/A)

**Value In Pipeline**

- Type: `kpi`
- Name: `3562065fddd9c2eb3aa5`
- Fields Used:
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Indicator)
  - `RELATIVE MONTH` (Query: `Opportunity Calendar.RELATIVE MONTH`) (Role: TrendLine)
- Visual Level Filters:
  - Filter on Unknown Target (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `a246f17b1ab3c41c6414`
- Fields Used: _(None detected)_

**0350598d17066b8e4060**

- Type: `None`
- Name: `0350598d17066b8e4060`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5f217d9743cb79b02a77`
- Fields Used: _(None detected)_

**lineChart**

- Type: `lineChart`
- Name: `91e80f5571abbccad3df`
- Fields Used:
  - `YEAR MONTH` (Query: `Opportunity Calendar.YEAR MONTH`) (Role: Category)
  - `Close %` (Query: `Opportunities.Close %`) (Role: Y)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Unknown)
- Visual Level Filters:
  - Filter on (Name: `Filter507b2c0ddf4f993cd933`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filterfce64fda3a5931380f90`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filterfd148b1dc07e587ec636`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter378449185421910ec48c`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter60848b3e0f6ed2da5bc9`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter17feaf997cb22073aec4`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filterb616ad48471799df27b7`) (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter41c0d4924d6c7028bb52`) (Type: N/A, Definition: N/A)

**lineChart**

- Type: `lineChart`
- Name: `998e81dde494d8e8be0d`
- Fields Used:
  - `Date` (Query: `Opportunity Calendar.Date`) (Role: Category)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Y)
  - `forecastValue` (Role: forecast.ForecastValue)
  - `confidenceHighBound` (Role: forecast.ConfidenceHighBound)
  - `confidenceLowBound` (Role: forecast.ConfidenceLowBound)
- Visual Level Filters:
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter65bf368e70c26ced0216`) (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `43250fc10b7a2e201ce2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8b0070cd050c48bce7cb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0d5db2c7c903a7ca9aa7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1ebceb3e55379e0b5493`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d1c03f8ddc9cb006bb4a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b9eac3f38aebdc64b1d9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `41c2d1b9175094a0e5a6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ca0451cee1c762d244b7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4e037b92b7d80b1bdd90`
- Fields Used: _(None detected)_

**lineChart**

- Type: `lineChart`
- Name: `44d9dc48f9786b7f27d8`
- Fields Used:
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Y)
  - `Date` (Query: `Opportunity Calendar.Date`) (Role: Category)
  - `ExpectedValue` (Role: anomalyDetection.ExpectedValue)
  - `ExpectedLow` (Role: anomalyDetection.ExpectedLow)
  - `ExpectedHigh` (Role: anomalyDetection.ExpectedHigh)
  - `RawScore` (Role: anomalyDetection.RawScore)
  - `Anomaly` (Role: anomalyDetection.Anomaly)
  - `BatchStart` (Role: anomalyDetection.BatchStart)
  - `BatchEnd` (Role: anomalyDetection.BatchEnd)
- Visual Level Filters:
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter65bf368e70c26ced0216`) (Type: N/A, Definition: N/A)

**lineChart**

- Type: `lineChart`
- Name: `c2d8c28b154bc6a841e2`
- Fields Used:
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Y)
  - `YEAR MONTH` (Query: `Opportunity Calendar.YEAR MONTH`) (Role: Category)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Unknown)
- Visual Level Filters:
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on (Name: `Filter17feaf997cb22073aec4`) (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `97ba045dcd8175880064`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `af653d89aaecee28245c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `36ad89da8c179d89030d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1b5ded2e2843c002ddbc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5695a808844203c59645`
- Fields Used: _(None detected)_

#### <a name="page-winloss-ratio-insights"></a>Page: Win/Loss Ratio Insights

*Internal Name: `ReportSection76c409e0c333d60bb1e2`, Ordinal: 5*

##### Page Level Filters

- Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter7`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter8`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter5`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter3`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter4`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter2`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter1`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter6`) (Type: N/A, Definition: N/A)

##### Visuals on this Page

**58a44374ac00e20debb7**

- Type: `None`
- Name: `58a44374ac00e20debb7`
- Fields Used: _(None detected)_

**e9f1d24f308635c7b74b**

- Type: `None`
- Name: `e9f1d24f308635c7b74b`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `80f141278d29b6cb5719`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2a170bf94dfa94fe00cd`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `03e3b50852edcc8445ae`
- Fields Used: _(None detected)_

**image**

- Type: `image`
- Name: `4cabbd60f663c913caa5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0b02c936c6d07e06439e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1c53cde851bd3e05e614`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `366b950342acf05f9a1b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `926309858dd9b4272310`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `de3eb39dd654a0ba8fd6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8c90f6765982f4898ada`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f08b9bbcc5486e1e60c0`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `0b02d573ee35221325dd`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cca86295937d77ea8239`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6954b4af41842bdcf262`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `af7099f1b462801e37b5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d96d32462ba6e9257f2a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `422247311a91e33be583`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6c0c40209ce5883633e4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2a709c9eb4f3e382d4da`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `af0038524d6a64320366`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `41260aa39364596d6c28`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cdc83dacf45a230af70c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3908d1c4568dfd613e80`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1248322628ecda260043`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `02d8321218d86db42fa3`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f9b4c5e1751ec2b60507`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0909f4e093367e2122fd`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `56e960b1f9c4bb3aa11e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ff38d5fe3972955ac20f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `77e4c73a5c00b3014436`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `403efab41564dca9fedf`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `92dea114ade90f95f4a9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `61c82aecd24fe3181aa8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3963388a089da17755db`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ccc25bc7751c05d989d4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `abaa931de076aa1bcc5a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ad8ec4f8c7362e8b9a08`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2fe5afd13d3a5d0370b4`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f4130e2fdd0688f6ebfc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f117db8694b15540843c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e872030b87e6f22a5d5e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `37d738413e78f319b392`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f0fa50ffb6dd150eb25c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `108324126af6f3751722`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7c570aec48c2b2af2303`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `063d39f3968092bdf5e4`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `1c2afa756a6f81bb2174`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `79263cb99d7a9eaac68f`
- Fields Used: _(None detected)_

**268b9361777451a42a01**

- Type: `None`
- Name: `268b9361777451a42a01`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c42326a3e7d6f193e6f9`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `0ff9e61d960d100dba8c`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `aa049c030e5a9cf7c0e0`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `a0044658c40aab9ffa6a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8cb03e680783605b03b2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `bbb9509eda04076550bb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `3cf525a0b2148a00a2ab`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b0e9eaa164722f37ebd4`
- Fields Used: _(None detected)_

**barChart**

- Type: `barChart`
- Name: `29eef36b9a38929aa54f`
- Fields Used:
  - `Product Category` (Query: `Products.Product Category`) (Role: Category)
  - `Close %` (Query: `Opportunities.Close %`) (Role: Y)

**actionButton**

- Type: `actionButton`
- Name: `075d886f06ca0142b119`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `440fae6f80de61117586`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `42f2bad1ae0ec28a42b7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `def0cd6efc79554f3a54`
- Fields Used: _(None detected)_

**keyDriversVisual**

- Type: `keyDriversVisual`
- Name: `ec80685720004c638d61`
- Fields Used:
  - `Opportunities.Status` (Role: Target)
  - `Avg(Opportunities.Discount)` (Role: ExplainBy)
  - `Opportunities.Purchase Process` (Role: ExplainBy)
  - `Owners.Owner` (Role: ExplainBy)
  - `Products.Product` (Role: ExplainBy)
  - `Owners.Manager` (Role: ExplainBy)
  - `Industries.Industry` (Role: ExplainBy)
  - `Campaigns.Name` (Role: ExplainBy)
- Visual Level Filters:
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)
  - Filter on Unknown Target (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `0b171fbb8e7cff5f903b`
- Fields Used: _(None detected)_

**5a182e590787407ff806**

- Type: `None`
- Name: `5a182e590787407ff806`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e22d8d1046b3d73945da`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `6f83dd34b2bd74299897`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ab8b2f68a2ff2868eab2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2a056dd34f7bd9e18a22`
- Fields Used: _(None detected)_

**lineStackedColumnComboChart**

- Type: `lineStackedColumnComboChart`
- Name: `01af2f16cdd3b0443588`
- Fields Used:
  - `Product Category` (Query: `Products.Product LOB`) (Role: Category)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Y)
  - `Close %` (Query: `Opportunities.Close %`) (Role: Y2)

**actionButton**

- Type: `actionButton`
- Name: `e9681a75c3377891eec6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `65a30f5c2fc6026ce09b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `bf5a36711fa34922a399`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `74ce63ea215ce37f730a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4cba0e9b52ec536a0ef2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `7fcfc6b35e4cef4c5a2f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e954bb0e2c56c5dbeabc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `072e11a281e45b215ca7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f144076440cdcec8f3e5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e53c1aa76a50b049856b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8a806043692871813231`
- Fields Used: _(None detected)_

#### <a name="page-winloss-ratio-overview"></a>Page: Win/Loss Ratio Overview

*Internal Name: `ReportSection3685d80df8fded83ed3c`, Ordinal: 1*

##### Page Level Filters

- Filter on (Name: `Filter4`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter1`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter3`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter2`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filter58495c8a81970d2c2350`) (Type: N/A, Definition: N/A)
- Filter on (Name: `Filterf6f8d6a01705e4bca438`) (Type: N/A, Definition: N/A)

##### Visuals on this Page

**actionButton**

- Type: `actionButton`
- Name: `67b743a30eb4a022cc40`
- Fields Used: _(None detected)_

**39ee217d1a3feec79d90**

- Type: `None`
- Name: `39ee217d1a3feec79d90`
- Fields Used: _(None detected)_

**952f79c232d6033955c6**

- Type: `None`
- Name: `952f79c232d6033955c6`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `63f8cd134d1b2c546e10`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `53b9a67fb93c5692e0c0`
- Fields Used: _(None detected)_

**image**

- Type: `image`
- Name: `25649a488729cedc5363`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ac62f676a07d29853d7d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e2fb139655e530359b2c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c45b604e457d3d1c3e10`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `18b726022b00c3b04a29`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fc1b1911699008a82ee8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b704bcf043dae960105c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ca449f093d8e0d3c7adb`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `2c2505a4ab12c00b51e5`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `05c06f7b0b771de4b776`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0a39b584a70ce9c3258`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d6f5b768689034dc9ab9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e11dc87a5c1da705967e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fdd9d8931902ba52ae27`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `716242218670d90de44e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `9b12fb7a4aa010d33a02`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a6b440c17ed6a5990e3d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f5111a3036e5dd01d41b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `12570bee86d7899035e8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `10b7ecd0dd4d0ab0628d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `2e53e95db60c4791408b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `cbe0c31e040d404ce165`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f30eaf60a2613daeadca`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `fc2c817088b08c604364`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `50cc21af2263adc00174`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ae8e7bef9e69c430044a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `f9b60ad25dd59b647401`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b5037f187db1920d0344`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c0d34fdfec56b4bd9040`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ab97766eaba10386c490`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `84a549b82ed0a72791cc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a5f089b902104bd53b7b`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0e95e681d06d4cd6c381`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `0282a0a7c510500063c9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1eb443d392c321593160`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1bba2b247d2e7d0bb948`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0dba8df4022750c13be`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e1df1862d08402d204e9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `05318827005c7840b1d8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `233a1b9a56b8804e7e8e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `b727dc9ed6772d0e0a8e`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1ffc8b819211899a6664`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `96b0564492d200096461`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `5eb8c7376d5575276ab9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `26430087360535b618ed`
- Fields Used: _(None detected)_

**a3aa481aa5b5b10dd30a**

- Type: `None`
- Name: `a3aa481aa5b5b10dd30a`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `345084ad874aa859652e`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `39b381f7ff73ea2f9384`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `dba1bbcce491ed77906b`
- Fields Used: _(None detected)_

**textbox**

- Type: `textbox`
- Name: `31c6d22ae72ea9c9090d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `c152ee6d24f605229982`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `e0c6b5e3c1e31e0dba2f`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1c52d135eada8a28bdbb`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1d2b32e2e6e245e25394`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `f41f2f87b47b937e76b8`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `0d27dd0157a15a1ab3c2`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `95f8915b7879ee034570`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `f07d80835a665c2499b9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `90d6c122090c45844405`
- Fields Used: _(None detected)_

**Forecast**

- Type: `kpi`
- Name: `8a0ce2360f3fa1944ab8`
- Fields Used:
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)
  - `Forecast by Win/Loss Ratio` (Query: `Opportunities.Forecast by Win/Loss Ratio`) (Role: Indicator)

**Revenue Won**

- Type: `kpi`
- Name: `32c088527926c965feeb`
- Fields Used:
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Indicator)

**All Open Revenue**

- Type: `kpi`
- Name: `c5c8a883a7a48a40a5eb`
- Fields Used:
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)
  - `Revenue Open` (Query: `Opportunities.Revenue Open`) (Role: Indicator)

**Win/Loss Percentage**

- Type: `kpi`
- Name: `fad4f0815aa586669b13`
- Fields Used:
  - `Blank` (Query: `Opportunities.Blank`) (Role: TrendLine)
  - `Close %` (Query: `Opportunities.Close %`) (Role: Indicator)

**0350598d17066b8e4060**

- Type: `None`
- Name: `0350598d17066b8e4060`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `a246f17b1ab3c41c6414`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5f217d9743cb79b02a77`
- Fields Used: _(None detected)_

**FlowVisual_C29F1DCC_81F5_4973_94AD_0517D44CC06A**

- Type: `FlowVisual_C29F1DCC_81F5_4973_94AD_0517D44CC06A`
- Name: `81457bc44662e94296df`
- Fields Used:
  - `systemuserid` (Query: `Owners.systemuserid`) (Role: table)

**Closing Percentages**

- Type: `clusteredColumnChart`
- Name: `bd762baaae85edc0f42f`
- Fields Used:
  - `Manager` (Query: `Owners.Manager`) (Role: Category)
  - `Owner` (Query: `Owners.Owner`) (Role: Category)
  - `Close %` (Query: `Opportunities.Close %`) (Role: Y)
- Visual Level Filters:
  - Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)

**Closing Percentages**

- Type: `barChart`
- Name: `d6c5d8ceebb55162083f`
- Fields Used:
  - `Product Category` (Query: `Products.Product LOB`) (Role: Category)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Tooltips)
  - `Product` (Query: `Products.Product`) (Role: Category)
  - `Close %` (Query: `Opportunities.Close %`) (Role: Y)
- Visual Level Filters:
  - Filter on (Name: `Filter`) (Type: N/A, Definition: N/A)

**actionButton**

- Type: `actionButton`
- Name: `43250fc10b7a2e201ce2`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `8b0070cd050c48bce7cb`
- Fields Used: _(None detected)_

**Win/Loss Ratio by Opportunity Owner**

- Type: `tableEx`
- Name: `e9ee7b2d33b6ec76638d`
- Fields Used:
  - `Close %` (Query: `Opportunities.Close %`) (Role: Values)
  - `Manager` (Query: `Owners.Manager`) (Role: Values)
  - `Owner` (Query: `Owners.Owner`) (Role: Values)
  - `Revenue Open` (Query: `Opportunities.Revenue Open`) (Role: Values)
  - `Forecast by Win/Loss Ratio` (Query: `Opportunities.Forecast by Win/Loss Ratio`) (Role: Values)

**actionButton**

- Type: `actionButton`
- Name: `0d5db2c7c903a7ca9aa7`
- Fields Used: _(None detected)_

**shape**

- Type: `shape`
- Name: `f7842f99d3c628076f33`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1ebceb3e55379e0b5493`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `d1c03f8ddc9cb006bb4a`
- Fields Used: _(None detected)_

**Revenue and forecast by Product**

- Type: `pivotTable`
- Name: `9f70be51c71a0fb66724`
- Fields Used:
  - `Products.Product LOB` (Role: Rows)
  - `Products.Product` (Role: Rows)
  - `Opportunities.Revenue Won` (Role: Values)
  - `Qualified Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Values)
  - `Opportunities.Forecast %` (Role: Values)

**actionButton**

- Type: `actionButton`
- Name: `b9eac3f38aebdc64b1d9`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `41c2d1b9175094a0e5a6`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `ca0451cee1c762d244b7`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `4e037b92b7d80b1bdd90`
- Fields Used: _(None detected)_

**lineChart**

- Type: `lineChart`
- Name: `610c93a9b6cdd51bffe6`
- Fields Used:
  - `Close %` (Query: `Opportunities.Close %`) (Role: Y)
  - `YEAR MONTH` (Query: `Opportunity Calendar.YEAR MONTH`) (Role: Category)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Unknown)
- Visual Level Filters:
  - Filter on (Name: `Filter02ce78c592feb6736c1e`) (Type: N/A, Definition: N/A)

**Closing Percentages**

- Type: `textbox`
- Name: `517971f6c10aacc974b8`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `97ba045dcd8175880064`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `af653d89aaecee28245c`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `36ad89da8c179d89030d`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `1b5ded2e2843c002ddbc`
- Fields Used: _(None detected)_

**actionButton**

- Type: `actionButton`
- Name: `5695a808844203c59645`
- Fields Used: _(None detected)_


---

