# Power BI Model & Report Documentation

*Generated on: 2025-06-25 13:21:06*

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

The Power BI data model appears to represent a comprehensive Customer Relationship Management (CRM) system focused on sales and marketing activities within a business context. The inclusion of tables such as 'Accounts', 'Contacts', 'Opportunities', and 'Campaigns' suggests a strong emphasis on managing customer relationships, tracking sales opportunities, and analyzing marketing efforts. The relationships between these tables indicate a structured approach to linking customer accounts with their respective contacts, sales opportunities, and marketing campaigns, facilitating a holistic view of customer interactions and sales performance.

Additionally, the presence of tables like 'Industries', 'Products', 'Territories', and 'Opportunity Calendar' highlights the model's capability to analyze sales data across different sectors, product lines, and geographical regions. The 'Opportunity Forecast Adjustment' table suggests a focus on refining sales forecasts based on various factors, enhancing decision-making processes. Overall, this data model is likely designed to empower business users with insights into sales trends, customer engagement, and marketing effectiveness, ultimately driving strategic growth and operational efficiency.

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

The 'Accounts' table serves as a comprehensive repository of customer account information, detailing key attributes such as account identifiers, geographic locations, and ownership, which enables businesses to analyze customer demographics, manage relationships, and optimize sales strategies across various territories and industries.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Account Name` | `string` | The 'Account Name' column stores the names of customer accounts, serving as a key identifier for managing and referencing account-related information within the Accounts table. |
| `Account Number` | `string` | The 'Account Number' column stores unique identifiers for each account, facilitating efficient tracking and management of customer accounts within the Accounts table. |
| `AccountID` | `string` | Column Description: A unique identifier for each account, represented as a string, used to facilitate account management and data retrieval within the Accounts table. |
| `AccountOwnerSeq` | `int64` | Column Description: The 'AccountOwnerSeq' column (int64) uniquely identifies the sequence number of the account owner associated with each account in the Accounts table. |
| `AccountSeq` | `int64` | Column Description: The 'AccountSeq' column (int64) uniquely identifies each account in the Accounts table, serving as a sequential reference for account management and tracking. |
| `Country` | `string` | The 'Country' column in the 'Accounts' table stores the name of the country associated with each account, facilitating geographic segmentation and analysis of account data. |
| `IndustrySeq` | `int64` | The 'IndustrySeq' column (int64) in the 'Accounts' table uniquely identifies the sequence number associated with the industry classification of each account, facilitating efficient categorization and analysis of industry-specific data. |
| `State or Province` | `string` | Column Description: This column captures the state or province associated with each account, facilitating regional analysis and reporting. |
| `TerritorySeq` | `int64` | Column Description: The 'TerritorySeq' column (int64) uniquely identifies the sequence number of the territory assigned to each account, facilitating efficient territory management and reporting. |

---

#### <a name="table-campaigns"></a>Table: `Campaigns`

The 'Campaigns' table serves as a centralized repository for tracking marketing initiatives, detailing each campaign's unique identifier, type, and name. This enables businesses to analyze campaign performance, optimize marketing strategies, and enhance overall engagement with target audiences.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Campaign` | `string` | The 'Campaign' column stores the names or identifiers of marketing campaigns, enabling the tracking and management of various promotional initiatives within the Campaigns table. |
| `Campaign Type` | `string` | Column Description: This column categorizes the nature of marketing initiatives, such as digital, print, or social media, to facilitate targeted analysis and reporting of campaign performance within the Campaigns table. |
| `CampaignSeq` | `int64` | Column Description: The 'CampaignSeq' column (int64) uniquely identifies the sequence number of each campaign within the 'Campaigns' table, facilitating the organization and retrieval of campaign data. |

---

#### <a name="table-contacts"></a>Table: `Contacts`

The 'Contacts' table serves as a centralized repository for managing key stakeholder information, including their job titles and unique identifiers, facilitating effective communication and relationship management across various accounts within the organization. This table enables businesses to streamline outreach efforts and enhance collaboration by providing easy access to essential contact details.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `AccountSeq` | `int64` | Column Description: The 'AccountSeq' column (int64) uniquely identifies the sequence number of the associated account for each contact, facilitating efficient data retrieval and relationship mapping within the Contacts table. |
| `Contact` | `string` | The 'Contact' column stores the names or identifiers of individuals or organizations associated with each entry in the Contacts table, facilitating effective communication and relationship management. |
| `ContactSeq` | `int64` | Column Description: A unique sequential identifier for each contact record in the Contacts table, facilitating efficient data retrieval and management. |
| `Job Title` | `string` | The 'Job Title' column captures the professional designation of each contact, providing essential context for understanding their role and responsibilities within their organization. |

---

#### <a name="table-industries"></a>Table: `Industries`

The 'Industries' table serves as a reference dataset that categorizes various sectors of the economy, enabling businesses to analyze performance metrics and trends by industry type. The inclusion of an industry sequence number facilitates efficient sorting and organization of industry data for reporting and analytical purposes.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Industry` | `string` | The 'Industry' column categorizes the various sectors in which businesses operate, providing essential context for analysis and reporting within the Industries table. |
| `IndustrySeq` | `int64` | Column Description: The 'IndustrySeq' column serves as a unique sequential identifier for each industry entry in the Industries table, facilitating efficient data retrieval and management. |

---

#### <a name="table-opportunities"></a>Table: `Opportunities`

The 'Opportunities' table serves as a critical resource for tracking and managing potential sales deals within the organization, providing insights into the purchase process, decision-making status, and sales progression. By analyzing key metrics such as deal value, probability of closure, and associated discounts, this table enables sales teams to prioritize efforts and forecast revenue more effectively.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `AccountSeq` | `int64` | The 'AccountSeq' column (int64) in the 'Opportunities' table uniquely identifies the sequence number of the associated account, facilitating the tracking and management of opportunities linked to specific accounts. |
| `CampaignSeq` | `int64` | Column Description: The 'CampaignSeq' column (int64) uniquely identifies the sequence number of marketing campaigns associated with each opportunity, facilitating the tracking and analysis of campaign effectiveness. |
| `CloseDate` | `dateTime` | The 'CloseDate' column represents the date and time when an opportunity is expected to be finalized or closed, serving as a critical timestamp for sales forecasting and performance tracking within the Opportunities table. |
| `DateDiff-Days` | `int64` | Column Description: This column represents the number of days between key dates in the opportunity lifecycle, facilitating analysis of time intervals for better decision-making and performance tracking. |
| `DaysToClose` | `int64` | The 'DaysToClose' column represents the number of days remaining until an opportunity is expected to be finalized, providing insights into the sales cycle duration for effective pipeline management. |
| `Decision Maker Identified` | `boolean` | Indicates whether a decision maker has been identified for the opportunity, facilitating targeted engagement strategies. |
| `Discount` | `double` | The 'Discount' column (double) in the 'Opportunities' table represents the monetary reduction applied to the total value of an opportunity, facilitating the assessment of pricing strategies and potential revenue adjustments. |
| `Opportunity Created On` | `dateTime` | The 'Opportunity Created On' column records the date and time when each sales opportunity was initiated, providing essential context for tracking the lifecycle and performance of opportunities within the sales pipeline. |
| `OpportunitySeq` | `int64` | Column Description: The 'OpportunitySeq' column, an integer identifier, uniquely tracks the sequence of each opportunity within the Opportunities table, facilitating efficient data management and retrieval. |
| `Probability` | `double` | The 'Probability' column (double) in the 'Opportunities' table represents the likelihood, expressed as a percentage, of successfully closing a sales opportunity, aiding in prioritization and forecasting efforts. |
| `Probability (raw)` | `double` | The 'Probability (raw)' column represents the unadjusted likelihood, expressed as a double value, of successfully closing a sales opportunity within the Opportunities table. |
| `ProductSeq` | `int64` | Column Description: The 'ProductSeq' column (int64) uniquely identifies the sequence of products associated with each opportunity, facilitating the tracking and management of product offerings within sales processes. |
| `Purchase Process` | `string` | The 'Purchase Process' column captures the current stage or steps involved in the sales cycle for each opportunity, providing insights into the progression and status of potential sales. |
| `Rating` | `string` | The 'Rating' column captures qualitative assessments of each opportunity, allowing stakeholders to gauge potential value and prioritize actions accordingly. |
| `Sales Stage` | `string` | The 'Sales Stage' column indicates the current phase of the sales process for each opportunity, helping to track progress and forecast potential revenue. |
| `Status` | `string` | The 'Status' column indicates the current stage or condition of each opportunity, providing essential insights for tracking progress and decision-making in the sales process. |
| `SystemUserSeq` | `int64` | Column Description: The 'SystemUserSeq' column (int64) uniquely identifies the system user associated with each opportunity, facilitating user-specific tracking and management within the Opportunities table. |
| `Value` | `int64` | The 'Value' column (int64) in the 'Opportunities' table represents the monetary worth or potential revenue associated with each opportunity, facilitating financial analysis and decision-making. |

##### Calculated Columns

**`Blank`** (`string`)

- **Description:** The 'Blank' column in the Opportunities table is intended for future use or optional notes, allowing for flexibility in data entry without impacting the integrity of existing records.
- **DAX Expression:**
```dax
BLANK()
```
- **DAX Explanation (Generated):** The DAX expression `BLANK()` is used to create a calculated column that contains no value, essentially representing an empty or null state. 

In simple business terms, when you use `BLANK()` in a calculated column, you are telling the system that for every row in that column, there should be no data recorded. This can be useful in various scenarios, such as:

1. **Placeholder for Future Data**: If you plan to fill in this column with data later, using `BLANK()` allows you to set up the structure without any initial values.

2. **Conditional Logic**: You might want to use `BLANK()` in conjunction with other calculations or conditions. For example, if certain criteria are not met, you can return `BLANK()` instead of a number or text, indicating that there is no applicable value.

3. **Data Cleaning**: If you are preparing your data for analysis and want to ensure that certain rows do not contribute to calculations or visualizations, marking them as `BLANK()` can help filter them out.

Overall, `BLANK()` is a way to explicitly define that there is no value present in that column for the rows where it is applied.

**`Days Remaining In Pipeline`** (`string`)

- **Description:** Column Description: This column indicates the number of days left for each opportunity to progress through the sales pipeline, helping stakeholders prioritize and manage their sales efforts effectively.
- **DAX Expression:**
```dax
IF(Opportunities[Status]="Open", DATEDIFF(TODAY(),Opportunities[CloseDate],DAY),0)
```
- **DAX Explanation (Generated):** This DAX code snippet is used to create a calculated column called "Days Remaining In Pipeline" for a dataset of opportunities. Here's a breakdown of what it does in simple business terms:

1. **Condition Check**: The expression starts by checking if the status of an opportunity is "Open". This means it only considers opportunities that are currently active and not yet closed.

2. **Calculate Days Remaining**: If the opportunity is "Open", it calculates the number of days remaining until the opportunity's close date. It does this by using the `DATEDIFF` function, which finds the difference between today's date (`TODAY()`) and the opportunity's `CloseDate`. The result is expressed in days.

3. **Return Value**: If the opportunity is not "Open" (meaning it might be closed or in another status), the expression returns 0. This indicates that there are no days remaining in the pipeline for opportunities that are not currently active.

### Summary:
In summary, this DAX expression calculates how many days are left until an open opportunity is expected to close. If the opportunity is not open, it simply returns 0. This helps businesses track how much time is left to convert open opportunities into sales, allowing for better pipeline management and forecasting.

**`Days Remaining In Pipeline (bins)`** (`string`)

- **Description:** Column Description: This column categorizes the remaining days in the sales pipeline into predefined bins, enabling quick assessment of opportunity urgency and prioritization for sales teams.

**`Weeks Open`** (`string`)

- **Description:** The 'Weeks Open' column indicates the duration, in weeks, that each opportunity has been active or available for engagement, represented as a string for flexible formatting.

##### Measures

**`Close %`**

- **DAX Expression:**
```dax
[Count of Won]/([Count of Won]+[Count of Lost])
```
- **DAX Explanation (Generated):** The DAX expression you provided calculates the "Close %" measure, which represents the percentage of successful outcomes (or "won" deals) compared to the total number of outcomes (both "won" and "lost" deals).

Here's a breakdown of the components:

1. **[Count of Won]**: This part counts the number of deals or opportunities that were successfully closed (won).

2. **[Count of Lost]**: This part counts the number of deals or opportunities that were not successful (lost).

3. **([Count of Won] + [Count of Lost])**: This adds together the number of won and lost deals to get the total number of deals that were either won or lost.

4. **[Count of Won] / ([Count of Won] + [Count of Lost])**: Finally, this divides the number of won deals by the total number of deals (won + lost). 

### What it Achieves:
The result of this calculation is a percentage that indicates how successful the team or organization is at closing deals. A higher percentage means a greater proportion of deals are being won, which is a positive indicator of performance. Conversely, a lower percentage suggests that there may be challenges in closing deals successfully.

In summary, this measure helps businesses understand their success rate in closing deals, which can inform strategies for improvement and performance evaluation.

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
- **DAX Explanation (Generated):** This DAX code snippet is designed to calculate the number of opportunities that have a status of "Lost" in a dataset called "Opportunities." Here’s a breakdown of what each part does in simple business terms:

1. **COUNTAX**: This function counts the number of rows that meet certain criteria. In this case, it will count the opportunities that are filtered based on their status.

2. **FILTER**: This function is used to create a subset of the data. It looks at the "Opportunities" table and filters it down to only those rows where the "Status" column equals "Lost." Essentially, it narrows down the dataset to just the opportunities that have been marked as lost.

3. **KEEPCFILTERS**: This function ensures that any existing filters on the "Opportunities" table are preserved while applying the new filter for lost opportunities. This means that if there are other filters applied (like date ranges or specific sales teams), they will still be considered in the calculation.

4. **Opportunities[OpportunitySeq]**: This refers to a specific column in the "Opportunities" table, which likely contains unique identifiers for each opportunity. The COUNTAX function will count the number of these unique identifiers in the filtered dataset.

### What It Achieves:
In summary, this DAX measure calculates the total number of opportunities that have been marked as "Lost," while also respecting any other filters that may be applied to the data. This is useful for businesses to understand how many potential sales did not close successfully, which can inform strategies for improvement in sales processes or customer engagement.

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
- **DAX Explanation (Generated):** This DAX code snippet is designed to create a measure called 'Count of Won' that calculates the number of opportunities that have been marked as "Won" in a dataset of sales opportunities. Here’s a breakdown of what each part does in simple business terms:

1. **COUNTAX**: This function counts the number of rows that meet certain criteria. In this case, it will count the opportunities that are filtered based on their status.

2. **FILTER**: This function is used to narrow down the dataset to only include the opportunities that meet specific conditions. Here, it filters the 'Opportunities' table to include only those rows where the status of the opportunity is "Won".

3. **KEEPCFILTERS**: This function ensures that any existing filters applied to the 'Opportunities' table remain in effect while adding the new filter for the "Won" status. This is important for maintaining the context of any other filters that might be applied in a report or dashboard.

4. **Opportunities[Status] = "Won"**: This condition checks each opportunity's status and only includes those that are marked as "Won".

5. **Opportunities[OpportunitySeq]**: This is the column that the COUNTAX function will count. It counts the number of unique sequences (or identifiers) of opportunities that have passed the filter criteria.

### In Summary:
The 'Count of Won' measure calculates the total number of sales opportunities that have been successfully won, while respecting any other filters that might be applied in the report. This helps businesses understand how many opportunities have resulted in successful sales, providing valuable insights into sales performance.

**`Forecast`**

- **DAX Expression:**
```dax
([Revenue Won]+[Revenue In Pipeline])
```
- **DAX Explanation (Generated):** This DAX expression calculates the total expected revenue by adding together two key components:

1. **Revenue Won**: This represents the actual revenue that has already been secured from sales or contracts that have been finalized. It reflects the money that the business has already earned.

2. **Revenue In Pipeline**: This refers to the potential revenue from sales opportunities that are currently being pursued but have not yet been finalized. This could include deals that are in negotiation or expected to close in the near future.

By summing these two values, the measure provides a forecast of total revenue, combining what has already been earned with what is anticipated to be earned soon. This helps businesses understand their current financial position and future revenue potential, aiding in planning and decision-making.

**`Forecast %`**

- **DAX Expression:**
```dax
(([Revenue Won]+[Revenue In Pipeline]))/ [Rev Goal]
```
- **DAX Explanation (Generated):** This DAX code snippet calculates the percentage of revenue that has been achieved or is expected to be achieved compared to a predefined revenue goal. Here’s a breakdown of what each part does:

1. **Revenue Won**: This represents the actual revenue that has been successfully earned or closed in a given period.

2. **Revenue In Pipeline**: This refers to the revenue that is expected to be earned from potential deals that are currently in progress but have not yet been finalized.

3. **Rev Goal**: This is the target revenue that the business aims to achieve within the same period.

### What the Calculation Achieves:

- **Total Revenue Calculation**: The expression first adds together the revenue that has already been won and the revenue that is still in the pipeline. This gives a total of both confirmed and potential revenue.

- **Percentage of Goal**: It then divides this total revenue by the revenue goal. This division calculates what percentage of the revenue goal has been met or is expected to be met.

### In Simple Terms:

The measure calculates how much of the revenue target has been achieved or is anticipated to be achieved by combining actual sales and potential sales, and then expressing that as a percentage of the overall revenue goal. This helps businesses understand their progress towards their financial targets and can inform decision-making and strategy adjustments.

**`Forecast by Win/Loss Ratio`**

- **DAX Expression:**
```dax
[Revenue Open] * [Close %]
```
- **DAX Explanation (Generated):** The DAX expression you provided is used to calculate a measure called "Forecast by Win/Loss Ratio." Let's break it down into simple terms:

1. **[Revenue Open]**: This part of the expression represents the total revenue that is currently open or in the pipeline. It could refer to potential sales that have not yet been finalized or closed.

2. **[Close %]**: This part represents the percentage likelihood that the open revenue will be successfully closed or converted into actual sales. It reflects the company's confidence in winning those potential deals.

3. **Multiplication**: By multiplying these two components together (`[Revenue Open] * [Close %]`), the expression calculates the expected revenue that the company anticipates will be realized from the open opportunities. 

### What It Achieves:
- **Forecasting Revenue**: This measure helps the business forecast how much revenue it can expect to earn based on the current open opportunities and the likelihood of closing those deals.
- **Decision-Making**: It provides valuable insights for sales and management teams to make informed decisions about resource allocation, sales strategies, and financial planning.
- **Performance Tracking**: By analyzing this measure over time, the business can track its performance in converting open opportunities into actual revenue, helping to identify trends and areas for improvement.

In summary, this DAX expression helps businesses estimate future revenue based on their current sales opportunities and the probability of closing those deals.

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
- **DAX Explanation (Generated):** This DAX code snippet is designed to create a measure called "Opportunity Count In Pipeline." Here's a breakdown of what it does in simple business terms:

1. **Purpose**: The measure counts the number of opportunities that are currently in an "Open" status within a dataset of opportunities.

2. **Key Components**:
   - **CALCULATE**: This function modifies the context in which data is evaluated. In this case, it is used to count opportunities based on specific criteria.
   - **COUNT(Opportunities[Value])**: This part counts the number of entries in the "Value" column of the "Opportunities" table. Essentially, it counts how many opportunities there are.
   - **FILTER**: This function is used to narrow down the data being counted. It specifies that only certain rows from the "Opportunities" table should be considered for counting.
   - **Opportunities[Status] = "Open"**: This condition within the FILTER function ensures that only opportunities that are marked as "Open" are included in the count.

3. **What It Achieves**: The measure calculates the total number of open opportunities in the pipeline. This is useful for sales teams and management to understand how many potential deals are still active and being pursued.

4. **Commented Out Code**: There is a commented-out line that suggests additional filtering could be applied to count only those opportunities that are in specific pipeline steps (like "3-Pipeline," "4-Mandate," or "5-Close"). If this line were active, it would further refine the count to only include opportunities at those stages, providing even more focused insights.

In summary, this DAX measure helps businesses track the number of active sales opportunities, which is crucial for managing sales performance and forecasting revenue.

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
- **DAX Explanation (Generated):** This DAX code snippet calculates a measure called "Revenue In Pipeline," which represents the potential revenue from sales opportunities that are currently open and at a certain stage in the sales process. Here’s a breakdown of what it does in simple business terms:

1. **Identify Open Opportunities**: The code first looks at a table called `Opportunities` to find all sales opportunities that are currently "Open." This means these are potential sales that have not yet been closed.

2. **Filter by Sales Stage**: It further narrows down these open opportunities by checking their "Sales Stage." Specifically, it only includes opportunities where the sales stage is at least 2 or higher. This implies that the opportunity is more advanced in the sales process and has a better chance of closing successfully.

3. **Calculate Total Value**: For the filtered list of open opportunities, the code calculates the total potential revenue by summing up the `Value` of each opportunity. This gives us the total revenue that could potentially be generated from these opportunities.

4. **Adjust for Forecasting**: After calculating the total revenue, the code applies a forecast adjustment. It takes the total revenue and increases it based on a percentage value found in another table called `Opportunity Forecast Adjustment`. This adjustment is expressed as a percentage (e.g., if the adjustment value is 10, it means increasing the revenue by 10%).

5. **Final Output**: The final result is the total potential revenue from open opportunities, adjusted for any forecast changes. This measure helps businesses understand how much revenue they can expect from their current sales pipeline, factoring in the likelihood of closing those deals.

In summary, this DAX measure provides a clear view of the expected revenue from open sales opportunities that are at a significant stage in the sales process, while also considering any adjustments based on forecasting.

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
- **DAX Explanation (Generated):** This DAX code snippet is designed to calculate the total revenue from opportunities that have been marked as "Won." Let's break it down step by step:

1. **SUMX(Opportunities, Opportunities[Value])**: This part of the code is calculating the total value of all opportunities. The `SUMX` function goes through each opportunity in the `Opportunities` table and sums up the values in the `Opportunities[Value]` column. Essentially, it adds up all the revenue amounts associated with each opportunity.

2. **FILTER(Opportunities, Opportunities[Status] = "Won")**: This part is filtering the opportunities to only include those that have a status of "Won." The `FILTER` function creates a subset of the `Opportunities` table, keeping only the rows where the `Status` column equals "Won." 

3. **CALCULATE(...)**: The `CALCULATE` function modifies the context in which the data is evaluated. In this case, it takes the total revenue calculated by `SUMX` and applies the filter created in the previous step. This means that instead of summing all opportunities, it will only sum the values of those that are "Won."

### In Summary:
The entire DAX expression calculates the total revenue from all opportunities that have been successfully won. It effectively answers the question: "What is the total revenue generated from opportunities that have been closed successfully?" This measure is useful for sales analysis, helping businesses understand their success in converting opportunities into actual revenue.

**`Revenue Won Average Deal Size`**

- **DAX Expression:**
```dax
AVERAGEX(Opportunities,[Revenue Won])
```
- **DAX Explanation (Generated):** The DAX expression you've provided calculates the average deal size of revenue won from opportunities. Let's break it down in simple terms:

1. **AVERAGEX**: This is a DAX function that calculates the average of a set of values. It takes two arguments: a table (or a set of rows) and an expression that defines what value to average.

2. **Opportunities**: This refers to a table or dataset that contains information about various sales opportunities. Each row in this table represents a different sales opportunity.

3. **[Revenue Won]**: This is a measure or column that represents the revenue that has been successfully won from each opportunity. It indicates how much money was generated from each sale that was closed.

Putting it all together, the expression `AVERAGEX(Opportunities,[Revenue Won])` does the following:

- It looks at all the opportunities in the "Opportunities" table.
- For each opportunity, it retrieves the value of revenue won.
- It then calculates the average of these revenue amounts.

**In business terms**, this measure provides insight into the average size of deals that have been successfully closed. It helps businesses understand how much revenue they typically earn from each successful sale, which can be useful for sales forecasting, performance analysis, and strategic planning.

---

#### <a name="table-opportunity-calendar"></a>Table: `Opportunity Calendar`

The 'Opportunity Calendar' table serves as a comprehensive time-based reference for tracking and analyzing business opportunities, enabling users to filter and segment data by various time dimensions such as day, week, month, and year. This structured calendar format facilitates effective reporting and forecasting, helping stakeholders identify trends and optimize decision-making processes related to sales and opportunity management.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Date` | `string` | The 'Date' column in the Opportunity Calendar table represents the scheduled date for each enrichment task, formatted as a string to facilitate easy readability and integration with various scheduling systems. |
| `DAY` | `string` | Column Description: The 'DAY' column represents the specific day of the week associated with each opportunity, facilitating the scheduling and tracking of calendar events within the Opportunity Calendar. |
| `DaySeq` | `string` | The 'DaySeq' column represents a sequential identifier for each day in the Opportunity Calendar, facilitating the organization and tracking of scheduled events or tasks. |
| `MONTH` | `string` | Column Description: The 'MONTH' column stores the name of the month associated with each opportunity, facilitating the organization and analysis of scheduling tasks within the Opportunity Calendar. |
| `MONTH NUMBER` | `string` | The 'MONTH NUMBER' column (string) in the 'Opportunity Calendar' table represents the numerical designation of each month, facilitating the organization and scheduling of opportunity-related activities throughout the year. |
| `RELATIVE 07 DAY PERIOD` | `string` | The 'RELATIVE 07 DAY PERIOD' column captures a string representation of a seven-day timeframe relative to the current date, facilitating the scheduling and tracking of opportunities within the Opportunity Calendar. |
| `RELATIVE 30 DAY PERIOD` | `string` | The 'RELATIVE 30 DAY PERIOD' column indicates the timeframe of the last 30 days relative to the current date, used for tracking and analyzing opportunity trends within the Opportunity Calendar. |
| `RELATIVE DAY` | `string` | The 'RELATIVE DAY' column in the Opportunity Calendar table represents a string identifier that indicates the specific day relative to a defined reference point, facilitating the scheduling and tracking of opportunity-related tasks. |
| `RELATIVE MONTH` | `string` | The 'RELATIVE MONTH' column in the Opportunity Calendar table indicates the month relative to the current date, facilitating the scheduling and tracking of opportunity-related activities over time. |
| `RELATIVE WEEK` | `string` | The 'RELATIVE WEEK' column indicates the specific week of the year relative to the current date, facilitating the scheduling and tracking of opportunity-related activities within the Opportunity Calendar. |
| `WEEK` | `string` | The 'WEEK' column (string) in the Opportunity Calendar table represents the specific week identifier for scheduling and tracking enrichment tasks related to business opportunities. |
| `YEAR` | `string` | The 'YEAR' column (string) in the 'Opportunity Calendar' table represents the specific year associated with each scheduled opportunity, facilitating time-based analysis and planning for enrichment tasks. |
| `YEAR MONTH` | `string` | The 'YEAR MONTH' column (string) in the Opportunity Calendar table represents the specific year and month associated with each scheduled opportunity, facilitating time-based analysis and reporting. |
| `YEAR MONTH NUMBER` | `string` | The 'YEAR MONTH NUMBER' column (string) in the Opportunity Calendar table represents the concatenated year and month in a standardized format, facilitating the organization and analysis of opportunities over time. |
| `YEAR WEEK` | `string` | The 'YEAR WEEK' column represents the specific year and week number for each opportunity, facilitating time-based analysis and scheduling of calendar events within the Opportunity Calendar table. |

---

#### <a name="table-opportunity-forecast-adjustment"></a>Table: `Opportunity Forecast Adjustment`

The 'Opportunity Forecast Adjustment' table is designed to capture and manage modifications to sales forecasts, enabling businesses to refine their revenue projections based on updated insights and strategic decisions. This table facilitates better alignment of sales strategies with market conditions, ultimately enhancing financial planning and resource allocation.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Forecast Adjustment` | `string` | The 'Forecast Adjustment' column captures qualitative notes or explanations regarding modifications made to the projected sales figures for opportunities, facilitating better understanding and analysis of forecast changes. |

##### Calculated Columns

**`Blank`** (`string`)

- **Description:** The 'Blank' column in the 'Opportunity Forecast Adjustment' table is intended for future use or optional notes, allowing users to input additional information or comments related to forecast adjustments without impacting the primary data structure.
- **DAX Expression:**
```dax
1
```
- **DAX Explanation (Generated):** The DAX expression you provided is simply the number `1`. In the context of a calculated column, this means that for every row in the table where this calculated column is created, the value of that column will be `1`.

### What it achieves:
- **Uniform Value**: Every row will have the same value of `1`. This can be useful for various purposes, such as:
  - **Counting**: If you want to count the number of rows in a table, you can sum this column, and it will give you the total number of rows.
  - **Flagging**: It can serve as a flag or marker to indicate that a certain condition is met for all rows.
  - **Grouping**: It can be used in calculations where you want to group data or perform operations that require a constant value.

In summary, this DAX expression creates a calculated column where every entry is `1`, which can be leveraged for counting or as a constant reference in further calculations.

##### Measures

**`Fcst adj slicer alt text`**

- **DAX Expression:**
```dax
CONCATENATE("Use the slicer to adjust the forecast, current value is ", 'Opportunity Forecast Adjustment'[Forecast Adjustment Value])
```
- **DAX Explanation (Generated):** This DAX code snippet creates a text message that provides guidance to users about how to interact with a forecast adjustment feature in a report or dashboard.

Here's a breakdown of what it does:

1. **CONCATENATE Function**: This function combines two pieces of text into one single string. In this case, it is used to create a complete message.

2. **Static Text**: The first part of the message is a fixed string: "Use the slicer to adjust the forecast, current value is ". This part informs the user that they can use a slicer (a filtering tool) to modify the forecast.

3. **Dynamic Value**: The second part of the message pulls in a dynamic value from a data field: `'Opportunity Forecast Adjustment'[Forecast Adjustment Value]`. This value represents the current forecast adjustment amount that has been set or selected by the user.

4. **Final Output**: When combined, the output of this DAX expression will be a complete sentence that tells the user what they can do (adjust the forecast using the slicer) and what the current adjustment value is. For example, if the current adjustment value is 100, the final message would read: "Use the slicer to adjust the forecast, current value is 100."

In summary, this DAX expression helps users understand how to interact with the forecast adjustment feature by providing them with real-time feedback on the current adjustment value.

**`Forecast Adjustment Value`**

- **DAX Expression:**
```dax
SELECTEDVALUE('Opportunity Forecast Adjustment'[Forecast Adjustment], 0)
```
- **DAX Explanation (Generated):** The DAX code snippet you provided is used to create a measure called 'Forecast Adjustment Value'. Here's a breakdown of what it does in simple business terms:

1. **Context of Use**: This measure is likely used in a report or dashboard that deals with sales opportunities and their forecast adjustments. It helps in understanding how much the forecast for sales opportunities has been adjusted.

2. **Functionality of SELECTEDVALUE**: The function `SELECTEDVALUE` is designed to return a single value from a column when there is only one value selected in the current context (like a filter or slicer). If there are multiple values selected or no values selected, it returns a default value, which in this case is `0`.

3. **What It Calculates**:
   - It looks at the column `'Opportunity Forecast Adjustment'[Forecast Adjustment]`, which presumably contains values representing adjustments made to sales forecasts.
   - If there is exactly one adjustment value selected (for example, if a user has filtered the data to a specific opportunity), it returns that specific adjustment value.
   - If there are multiple adjustment values selected or none at all, it returns `0`.

4. **Business Impact**: This measure helps users quickly see the specific forecast adjustment for a selected opportunity. If no specific adjustment is selected, it defaults to `0`, indicating that there is no adjustment to consider. This is useful for reporting and analysis, as it allows users to focus on relevant adjustments without confusion from multiple or absent values.

In summary, this DAX expression helps in retrieving a specific forecast adjustment value for analysis, ensuring clarity in reporting by providing a default value when necessary.

---

#### <a name="table-owners"></a>Table: `Owners`

The 'Owners' table captures key information about individuals responsible for various assets or projects within the organization, detailing their names, managerial relationships, and unique identifiers. This data is essential for tracking accountability and facilitating communication across teams, enhancing overall operational efficiency.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Manager` | `string` | The 'Manager' column identifies the individual responsible for overseeing the owners listed in the table, facilitating accountability and communication within the organization. |
| `Owner` | `string` | The 'Owner' column identifies the individual or entity responsible for managing or overseeing the associated records within the Owners table. |
| `systemuserid` | `string` | The 'systemuserid' column stores the unique identifier for each owner in the Owners table, facilitating the association of ownership records with specific users in the system. |
| `SystemUserSeq` | `int64` | Column Description: The 'SystemUserSeq' column (int64) uniquely identifies the sequence number of the system user associated with each owner record in the Owners table. |

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
- **DAX Explanation (Generated):** This DAX code snippet is designed to calculate a revenue goal for a business based on current opportunities in the sales pipeline and previously won revenue. Here’s a breakdown of what it does in simple business terms:

1. **Calculate Revenue in Pipeline**:
   - The first part of the code defines a variable called `RevenueInPipeline`. This variable calculates the total value of all sales opportunities that are currently "Open" and have a sales stage that is at least a certain level (indicated by the first character of the `Sales Stage` being 2 or higher).
   - Essentially, it sums up the potential revenue from opportunities that are still in the sales process and are considered viable.

2. **Calculate Base Goal**:
   - The next part of the code defines another variable called `BaseGoal`. This variable takes the total revenue that has already been won (`Revenue Won`) and adds 60% of the `RevenueInPipeline` calculated earlier. 
   - The result is then rounded to the nearest million dollars using the `MROUND` function. This rounding helps in setting a more manageable and realistic revenue goal.

3. **Return the Final Goal**:
   - Finally, the code checks if the `BaseGoal` is greater than zero. If it is, it returns this value as the final revenue goal. If the `BaseGoal` is zero or less, it calculates a slightly adjusted goal by rounding the sum of `Revenue Won` and 60% of `RevenueInPipeline` to the nearest hundred thousand instead.
   - This ensures that there is always a positive revenue goal, even if the calculated base goal is not favorable.

### Summary:
In summary, this DAX measure calculates a revenue goal by considering both the revenue already won and a portion of the potential revenue from open sales opportunities. It ensures that the goal is rounded to a practical figure and always returns a positive target for the business to aim for.

---

#### <a name="table-products"></a>Table: `Products`

The 'Products' table serves as a comprehensive inventory catalog, detailing each product's unique identifier, sequence number, and associated category, enabling businesses to efficiently manage and analyze their product offerings for improved sales strategies and inventory control.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Product` | `string` | The 'Product' column contains the names of items available for sale, serving as a key identifier for inventory management and sales tracking within the Products table. |
| `Product Category` | `string` | Column Description: This column categorizes each product into specific groups, enabling streamlined inventory management and targeted marketing strategies. |
| `ProductSeq` | `int64` | Column Description: The 'ProductSeq' column serves as a unique sequential identifier for each product in the 'Products' table, facilitating efficient data retrieval and management. |

---

#### <a name="table-territories"></a>Table: `Territories`

The 'Territories' table provides a structured overview of geographical divisions within a business's operational landscape, detailing regions, countries, and states or provinces to facilitate targeted sales strategies and resource allocation. By organizing territories with unique identifiers, this table supports effective market analysis and performance tracking across different locations.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Country` | `string` | Column Description: This column stores the name of the country associated with each territory, facilitating geographic categorization and analysis of regional data. |
| `Region` | `string` | The 'Region' column identifies the geographical area associated with each territory, facilitating regional analysis and strategic planning. |
| `State Or Province` | `string` | Column Description: The 'State Or Province' column captures the name of the specific state or province within a territory, facilitating geographic identification and regional analysis. |
| `Territory` | `string` | The 'Territory' column identifies specific geographic regions or areas assigned for sales, marketing, or operational purposes within the Territories table. |
| `TerritorySeq` | `string` | The 'TerritorySeq' column stores a unique string identifier for each territory, facilitating efficient tracking and management of territorial data within the Territories table. |

---

## <a name="report-structure"></a>Report Structure

_No report-level filters found._

### <a name="report-pages"></a>Report Pages

#### <a name="page-days-to-close-insights"></a>Page: Days to Close Insights

*Internal Name: `ReportSectionf0c8ef19be5e8127c627`, Ordinal: 6*

##### Page Level Filters

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: In simple business terms, this Power BI filter is used to focus on specific types of opportunities based on their status. 

Here's what the filter does:

- **Target Field**: The filter is applied to the `Status` field of the `Opportunities` data.
- **Included Values**: The filter specifies that only opportunities with a status of either **'Lost'** or **'Won'** should be included in the analysis or report.
- **Excluded Values**: Any opportunities that have a status other than 'Lost' or 'Won' (such as 'Pending', 'In Progress', or any other status) will be excluded from the data being analyzed.

In summary, this filter helps you to narrow down your view to only those opportunities that have been either lost or won, allowing for a more focused analysis of outcomes.)
- Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Decision Maker Identified` within the `Opportunities` dataset. This field likely indicates whether a decision maker has been identified for a particular opportunity.

2. **Filter Type**: The filter is set to "(All values)". This means that no specific criteria are being applied to the `Decision Maker Identified` field.

3. **Data Inclusion**: Since the filter includes all values, it means that every opportunity, regardless of whether a decision maker has been identified or not, will be included in the report. 

4. **No Exclusions**: There are no exclusions in this filter. Opportunities with a decision maker identified and those without will both be shown.

### Summary:
In simple terms, this filter allows you to see all opportunities in your report, without filtering out any based on whether a decision maker has been identified. You will get a complete view of all opportunities, which can be useful for comprehensive analysis or reporting.)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Context**: The filter is applied to the `Opportunities` table, specifically focusing on the `Purchase Process` field.

2. **What It Means**: The filter `"(All values)"` indicates that **all possible values** for the `Purchase Process` field are included in the data being analyzed. This means that no specific criteria are being applied to limit the data; every opportunity, regardless of its purchase process stage, will be considered.

3. **Data Inclusion**: Since the filter includes all values, it does not exclude any opportunities based on their purchase process status. For example, whether an opportunity is in the initial stage, negotiation, or closed won/lost, all of these will be part of the analysis.

### Summary:
In simple terms, this filter allows you to see **everything** related to the `Purchase Process` in the `Opportunities` data. There are no restrictions, so you get a complete view of all opportunities without filtering out any specific stages or statuses.)
- Filter on `Industries`.`Industry` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: This filter is set to include **all values** for the field `Industries.Industry`. 

2. **Data Included**: When this filter is applied, it does not exclude any industries. This means that every industry in your dataset will be shown in the report or visualization. 

3. **No Exclusions**: Since the filter is set to "All values," there are no restrictions or limitations on the data. You will see a complete view of all industries without any filtering out of specific ones.

### Summary:
In simple terms, this filter allows you to see every industry available in your data, ensuring that no industry is left out of your analysis.)
- Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are focusing on the data related to the managers of the owners in your dataset.

2. **Filter Definition**: The term "(All values)" indicates that **no specific filtering is being applied**. This means that all managers will be included in the data being analyzed or displayed.

### What This Means for Your Data:

- **Inclusion**: Every manager in the dataset will be included in the report or visualization. There are no restrictions or exclusions based on manager names or any other criteria.
  
- **No Exclusion**: Since the filter is set to include all values, you will not miss any data related to any manager. This is useful when you want a comprehensive view of all managers without narrowing down to specific ones.

### Summary:

In summary, applying this filter means you are looking at data for **all managers** without any limitations. This is helpful when you want to analyze overall performance or trends across all managers in your organization.)
- Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Owner`. This means we are focusing on the data related to the owners of certain items, assets, or entities in your dataset.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `Owners.Owner` field. This means that all owners will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter is set to include "(All values)", every owner in the dataset will be considered. There are no restrictions or exclusions based on owner names or categories.

### Summary:
When this filter is applied, it ensures that all owners are included in your analysis, allowing you to see the complete picture without omitting any specific owner from the dataset. This is useful when you want to analyze data across all owners without any bias or limitation.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when you apply this filter, you are not excluding any categories of products. Every product category available in your dataset will be shown in your reports.

2. **Data Included**: Since the filter is set to "(All values)", all product categories—such as Electronics, Clothing, Home Goods, etc.—will be included in the analysis. There are no restrictions on which categories are displayed.

3. **Data Excluded**: There are no exclusions with this filter. No product categories are left out; everything is included.

### Summary:
When you apply this filter to the `Products`.`Product Category`, you will see a complete view of all product categories without any limitations. This is useful when you want to analyze or report on the entire range of products without filtering out any specific categories.)
- Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Products`.`Product`. This means that no specific products are being excluded or filtered out.

2. **Data Inclusion**: When this filter is applied, every product in the dataset will be shown. There are no restrictions or conditions limiting which products can appear in your reports.

3. **Use Case**: This type of filter is useful when you want to see a complete overview of all products without any segmentation or filtering. For example, if you are analyzing total sales across all products, using this filter ensures that you are considering every product in your analysis.

### Summary:
In summary, the filter "(All values)" means that all products will be included in the analysis, allowing for a comprehensive view of the data without any exclusions.)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Opportunities.Purchase Process`. This means that no specific criteria are being applied to limit the data shown.

2. **Data Included**: When this filter is applied, every opportunity in the dataset will be considered, regardless of its purchase process stage. This includes all stages such as "Lead," "Proposal," "Negotiation," "Closed Won," and "Closed Lost," or any other stages defined in your data.

3. **Data Excluded**: Since the filter is set to include all values, there are no exclusions. Every opportunity will be visible in the report, and no data will be left out based on the purchase process.

### Summary:
In simple terms, this filter allows you to see **everything** related to the purchase process of opportunities without any restrictions. It’s like saying, "Show me all opportunities, no matter what stage they are in.")

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
  - Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Products.Product`. This means that no specific criteria are being applied to limit the data.

2. **Data Included**: When this filter is applied, every single product in the `Products` dataset will be included in the analysis. There are no exclusions or restrictions, so you will see all products regardless of their attributes (like category, price, availability, etc.).

3. **Use Case**: This type of filter is useful when you want to analyze the overall performance or characteristics of all products without narrowing down to specific segments. For example, if you are looking at total sales, customer feedback, or inventory levels, you would want to see data for every product.

### Summary:
The filter `(All values)` means that all products will be included in your analysis, allowing you to view comprehensive data without any limitations.)
  - Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Owners.Owner`. This means that no specific owners are being excluded or included; instead, every owner in the dataset will be considered.

2. **Data Inclusion**: When this filter is applied, it ensures that all owners are shown in the report or visualization. For example, if you have a list of owners like "Alice," "Bob," and "Charlie," all of them will be included in the analysis.

3. **No Exclusions**: Since the filter is set to "(All values)," there are no restrictions or exclusions. This means that even if there are owners with no data or those that might typically be filtered out, they will still be part of the results.

### Summary:
In summary, this filter allows you to see data for every owner without any limitations. It provides a comprehensive view of all owners in your dataset, ensuring that no one is left out of the analysis.)
  - Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are focusing on the data related to the managers of owners in your dataset.

2. **Filter Action**: The term "(All values)" indicates that **no specific filtering is being applied**. This means that all managers will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter is set to include all values, every manager in the dataset will be considered. There are no exclusions or restrictions based on specific criteria.

### Summary:
When this filter is applied, it ensures that all managers are included in the analysis, allowing you to see data related to every manager without any limitations. This is useful when you want a comprehensive view of all managers and their associated data, rather than focusing on a subset of them.)
  - Filter on `Accounts`.`State or Province` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Accounts`.`State or Province`. This field typically contains information about the geographical locations of accounts, such as states or provinces.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `State or Province` field. This means that all states or provinces will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter is set to include "(All values)", every account from every state or province will be shown in the report. There are no restrictions or exclusions based on geographical location.

### Summary:
In simple terms, this filter allows you to see data from all states or provinces without excluding any specific locations. It ensures that the analysis includes every account, regardless of where it is located.)
  - Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the `Purchase Process` field within the `Opportunities` dataset.

2. **Filter Type**: The filter is set to include **all values**. This means that no specific criteria are being applied to limit the data.

3. **Data Inclusion**: Since the filter is set to "(All values)", every single entry in the `Purchase Process` field will be included in the analysis. This means that all opportunities, regardless of their purchase process stage (e.g., prospecting, negotiation, closed-won, closed-lost), will be visible in your reports.

4. **Data Exclusion**: There are no exclusions with this filter. No opportunities are being filtered out, so you will see a complete view of all opportunities related to the purchase process.

### Summary:
In summary, this filter allows you to see all opportunities in the `Purchase Process` without any restrictions. It provides a comprehensive view of the data, ensuring that every opportunity is considered in your analysis.)
  - Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Decision Maker Identified` within the `Opportunities` dataset. This field likely indicates whether a decision maker has been identified for a particular opportunity.

2. **Filter Action**: The filter specifies "(All values)", which means that it does not exclude any data. Instead, it includes every possible value from the `Decision Maker Identified` field.

3. **Data Impact**: When this filter is applied, all opportunities will be shown, regardless of whether a decision maker has been identified or not. There are no restrictions on the data being displayed.

### Summary:
In simple terms, this filter ensures that all opportunities are included in your report, whether or not a decision maker has been identified. It does not filter out any records, allowing you to see the complete picture of your opportunities.)

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

- Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to control which data is included in your analysis based on the `RELATIVE MONTH` field from the `Opportunity Calendar`. Let's break it down in simple terms:

1. **`RELATIVE MONTH` > -18**: This part of the filter means that we are only interested in opportunities that have a `RELATIVE MONTH` value greater than -18. In practical terms, this means we are looking at data from the last 18 months, starting from the current month. For example, if today is October 2023, this filter will include data from May 2022 onwards.

2. **NOT (`RELATIVE MONTH` = null)**: This part of the filter ensures that we do not include any records where the `RELATIVE MONTH` value is null (or missing). In other words, if there is no month information available for an opportunity, that record will be excluded from the analysis.

### Summary:
When this filter is applied, it includes only those opportunities that have a `RELATIVE MONTH` value indicating they occurred within the last 18 months and excludes any opportunities that do not have a specified month. This helps focus the analysis on recent opportunities while ensuring that all included data is complete and relevant.)
- Filter on `Opportunities`.`Sales Stage` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the `Sales Stage` field within the `Opportunities` dataset. This field typically represents different stages in the sales process, such as "Prospecting," "Negotiation," "Closed Won," etc.

2. **Filter Action**: The filter is set to include **all values** from the `Sales Stage` field. This means that when this filter is applied, it does not exclude any sales stages. 

3. **Data Impact**: As a result, every opportunity, regardless of its current sales stage, will be included in the analysis or report. You will see data for all opportunities, whether they are at the beginning of the sales process or have already been closed.

### Summary:
In simple terms, this filter allows you to see all opportunities in your report, without filtering out any specific sales stages. It ensures that no data is excluded based on the sales stage, giving you a complete view of all opportunities.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the `Product Category` field within the `Products` dataset.

2. **Filter Type**: The filter is set to include **all values** from the `Product Category` field. This means that when this filter is applied, it does not exclude any categories of products.

3. **Data Inclusion**: Since the filter specifies "(All values)", every product category available in the dataset will be included in the report or visualization. For example, if your product categories include "Electronics," "Clothing," and "Home Goods," all of these categories will be shown.

4. **No Exclusions**: There are no restrictions or exclusions applied to the data. This means that the report will reflect the complete picture of all product categories without filtering out any specific category.

### Summary:
In simple terms, this filter ensures that all product categories are visible in your Power BI report, allowing users to see data for every category without any limitations.)
- Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Owner`. This means we are focusing on the data related to the owners of certain items, assets, or responsibilities in your dataset.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `Owners.Owner` field. This means that all owners will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter is set to include "(All values)", every owner in the dataset will be considered. There are no restrictions or exclusions, so all records related to every owner will be shown in your reports.

### Summary:
In simple terms, this filter allows you to see data for **all owners** without excluding anyone. It ensures that every owner is represented in the analysis, providing a complete view of the data related to ownership.)
- Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Products.Product`. This means that no specific criteria are applied to limit the data shown.

2. **Data Included**: When this filter is applied, every single product in the `Products` dataset will be included in the report or visualization. There are no exclusions or restrictions based on product attributes, categories, or any other criteria.

3. **Data Excluded**: Since the filter is set to include all values, there are no products being excluded. Every product that exists in the dataset will be visible.

### Summary:
In simple terms, this filter ensures that all products are displayed without any limitations. It allows users to see the complete list of products available in the dataset, making it useful when you want to analyze or report on the entire product range without filtering out any specific items.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when this filter is applied, no categories are excluded from the data being analyzed or displayed.

2. **Data Inclusion**: Every single product category available in your dataset will be shown. For example, if you have categories like "Electronics," "Clothing," and "Home Goods," all of these categories will be included in your report.

3. **No Exclusions**: Since the filter specifies "(All values)," there are no restrictions or limitations on the data. This is useful when you want to see a comprehensive view of all product categories without filtering out any specific ones.

### Summary:
In summary, this filter allows you to see all product categories in your Power BI report, ensuring that no data is left out. It’s a way to ensure a complete overview of your product offerings.)
- Filter on `Industries`.`Industry` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Industries.Industry`. This means that no specific industries are being excluded or included; instead, every industry available in the dataset will be shown.

2. **Data Impact**: When this filter is applied, it does not limit the data in any way. For example, if your dataset includes industries like "Technology," "Healthcare," "Finance," etc., all of these industries will be visible in your reports. 

3. **Use Case**: This type of filter is useful when you want to analyze or visualize data across all industries without any restrictions. It allows for a comprehensive view of the data, making it easier to identify trends or patterns across the entire dataset.

### Summary:
In summary, the filter `(All values)` means that you are looking at every industry in your dataset without any exclusions, allowing for a complete analysis of all available data related to industries.)
- Filter on `Industries`.`IndustrySeq` (Type: Advanced, Explanation: In simple business terms, this Power BI filter definition is used to refine the data being analyzed by excluding certain records based on the `IndustrySeq` field.

Here's what the filter does:

1. **Excludes IndustrySeq = 0**: This means that any records where the `IndustrySeq` is equal to 0 will not be included in the analysis. Essentially, if an industry has a sequence number of 0, it will be ignored.

2. **Excludes IndustrySeq = null**: This part of the filter means that any records where the `IndustrySeq` is missing or not defined (i.e., null) will also be excluded from the analysis. If there is no sequence number assigned to an industry, that record will not be considered.

In summary, when this filter is applied, only records with a valid `IndustrySeq` (meaning it is neither 0 nor null) will be included in the data analysis. This helps ensure that the analysis focuses on industries that have meaningful sequence numbers, thereby improving the quality and relevance of the insights derived from the data.)

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
  - Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are focusing on the data related to the managers of owners in your dataset.

2. **Filter Type**: The filter is set to "(All values)". This indicates that there are no restrictions being applied to the data for the `Owners.Manager` field.

3. **Data Inclusion**: Since the filter is set to include all values, it means that every manager in the dataset will be included in the analysis. No managers are excluded, and all associated data will be visible.

### Summary:
In simple terms, this filter allows you to see data for every manager without any limitations. You will have a complete view of all managers and their related information in your reports.)
  - Filter on `Opportunities`.`[Opportunity Count]` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field it is applied to. In this case, it means that no specific criteria are being applied to limit the data.

2. **Impact on Data**: When this filter is applied to the target `Opportunities.[Opportunity Count]`, it means that every opportunity in the dataset will be counted. There are no exclusions or restrictions, so all opportunities will be considered in the total count.

3. **Result**: As a result, when you look at the `Opportunity Count`, you will see the total number of opportunities available in the dataset without any filtering. This is useful when you want to get a complete view of all opportunities without narrowing down to specific segments or criteria.

### Summary:
In summary, the filter "(All values)" ensures that every opportunity is included in the count, providing a comprehensive overview of the total opportunities available.)
  - Filter on `Opportunities`.`[Revenue Won]` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field it is applied to, which in this case is `Opportunities.[Revenue Won]`. 

2. **Data Included**: This means that every single opportunity, regardless of how much revenue was won, will be considered in the analysis. There are no restrictions or exclusions based on revenue amounts.

3. **No Exclusions**: Since the filter is set to "All values," it does not exclude any opportunities based on their revenue won. Whether an opportunity has won $0, $1,000, or $1,000,000, all of them will be included in the data being analyzed.

### Summary:
When this filter is applied to `Opportunities.[Revenue Won]`, it ensures that all opportunities are taken into account, allowing for a comprehensive view of the data without any limitations based on revenue amounts. This is useful when you want to analyze the overall performance or trends without filtering out any specific revenue ranges.)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: In simple business terms, the provided filter definition JSON is specifying a condition for the `RELATIVE MONTH` field in the `Opportunity Calendar` data.

Here's what it means:

- **`RELATIVE MONTH`**: This is a field that likely represents the month relative to the current date. For example, it could indicate the current month as `0`, the previous month as `-1`, the next month as `1`, and so on.

- **`>= 0`**: This part of the filter means "greater than or equal to zero." 

When this filter is applied, it includes all records where the `RELATIVE MONTH` is **0 or greater**. In practical terms, this means:

- **Included Data**: 
  - The current month (where `RELATIVE MONTH` is `0`).
  - Future months (where `RELATIVE MONTH` is `1`, `2`, etc.).

- **Excluded Data**: 
  - Any past months (where `RELATIVE MONTH` is `-1`, `-2`, etc.).

So, in summary, this filter is used to focus on opportunities that are happening in the current month and any future months, while excluding any opportunities that occurred in the past.)
  - Filter on `Opportunity Calendar`.`YEAR MONTH` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Opportunity Calendar`.`YEAR MONTH`. This field likely contains information about the year and month of various opportunities (like sales or projects) in your dataset.

2. **Filter Type**: The filter is set to "(All values)". This means that no specific criteria are being applied to the `YEAR MONTH` field.

3. **Data Inclusion**: Since the filter includes "All values," it means that every single entry in the `YEAR MONTH` field will be included in the analysis. There are no restrictions or exclusions based on the year or month.

### Summary:

When this filter is applied, you will see data for every month and year available in your dataset. It does not limit or filter out any specific months or years, allowing you to analyze the complete range of opportunities without any time-based restrictions.)

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
  - Filter on `Accounts`.`Account Name` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Accounts.Account Name`. This means that when you apply this filter, you are not excluding any account names from your analysis.

2. **Data Included**: Every single account name in the `Accounts` table will be shown in your report or visualization. There are no restrictions or conditions applied to limit which account names are displayed.

3. **Data Excluded**: Since the filter includes all values, there are no account names being excluded. You will see every account that exists in the dataset.

### Summary:
In simple terms, this filter ensures that you are looking at the complete list of account names without omitting any. It’s like saying, “Show me everything related to account names.”)
  - Filter on `Opportunities`.`[Close %]` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Opportunities.[Close %]`. This means that when this filter is applied, it does not restrict or limit the data based on the `Close %` values.

2. **Data Included**: Every opportunity, regardless of its `Close %`, will be included in the analysis. This means you will see opportunities with a `Close %` of 0%, 50%, 100%, and everything in between.

3. **Data Excluded**: Since the filter is set to include all values, there are no exclusions. No opportunities are filtered out based on their `Close %`.

### Summary:
When you apply this filter to the `Opportunities.[Close %]`, you are ensuring that all opportunities are considered in your analysis, providing a complete view of the data without any restrictions based on the closing percentage.)
  - Filter on `Industries`.`Industry` (Type: TopN, Explanation: The provided filter definition JSON, which reads "`Industry` IN ()", is essentially saying that we want to filter the data based on the `Industry` field, but it currently has no values specified within the parentheses.

In simple business terms, this means:

- **Target Field**: We are looking at the `Industry` column in our dataset.
- **Filter Condition**: The filter is set to include only those records where the `Industry` matches certain specified values.
- **Current State**: Since the parentheses are empty (i.e., `IN ()`), it means there are no industries specified for inclusion.

### What This Means for Data:
- **Included Data**: No industries will be included because there are no values listed.
- **Excluded Data**: All industries will be excluded from the results because the filter does not allow any industry to pass through.

### Conclusion:
In practical terms, applying this filter will result in **no data being displayed** because there are no industries defined to include. It effectively acts as a filter that blocks all records related to the `Industry` field.)
  - Filter on `Industries`.`Industry` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Industries`.`Industry`. This means we are looking at the data related to different industries.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific restrictions** are being placed on the data. In other words, this filter is saying, "Include all industries without excluding any."

3. **Data Inclusion**: When this filter is applied, every industry in the dataset will be included in the report or visualization. There are no limitations or exclusions based on industry type.

### Summary:
This filter allows you to see data from all industries, ensuring that you have a complete view without filtering out any specific industry.)
  - Filter on `Opportunities`.`[Revenue Won]` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field it is applied to, which in this case is `Opportunities.[Revenue Won]`.

2. **Data Included**: This means that every single opportunity, regardless of the revenue amount, will be considered in the analysis. There are no restrictions or exclusions based on revenue.

3. **No Exclusions**: Since the filter is set to "All values," it does not exclude any opportunities based on their revenue. Whether an opportunity has a revenue of $0, $10,000, or $1,000,000, all of them will be included in the results.

### Summary:
When this filter is applied to `Opportunities.[Revenue Won]`, it ensures that all opportunities are taken into account, allowing for a comprehensive view of the data without any filtering based on revenue amounts. This is useful when you want to analyze the total revenue won across all opportunities without missing any data points.)

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
  - Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are focusing on the data related to the managers of owners in your dataset.

2. **Filter Type**: The filter is set to "(All values)". This indicates that no specific restrictions are being applied to the data. 

3. **Data Inclusion**: By using "(All values)", the filter includes every possible value for the `Owners.Manager` field. This means that all managers, regardless of their specific names or characteristics, will be included in the analysis.

4. **Data Exclusion**: Since the filter is set to include all values, there are no exclusions. Every manager in the dataset will be considered, and none will be left out.

### Summary:
In simple terms, this filter means that when you look at the data related to `Owners.Manager`, you will see information for every manager without any limitations or exclusions. All managers are included in the analysis, allowing for a comprehensive view of the data.)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: In simple business terms, the filter definition JSON you provided is specifying a condition for the `RELATIVE MONTH` field in the `Opportunity Calendar` data. 

Here's what it means:

- **`RELATIVE MONTH`**: This is a field that likely represents the month relative to the current date. For example, it could indicate the current month as `0`, the previous month as `-1`, the next month as `1`, and so on.

- **`>= 0`**: This part of the filter means "greater than or equal to zero." 

Putting it all together, this filter is including all data where the `RELATIVE MONTH` is **the current month (0)** or **any future months (1, 2, etc.)**. 

In practical terms, when this filter is applied, you will see opportunities that are happening now or are planned for the future, but you will **exclude** any opportunities that occurred in the past (like last month or earlier). 

So, if you were looking at a report or dashboard, you would only see opportunities that are relevant to the present and future, helping you focus on what’s upcoming rather than what has already happened.)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: The provided filter definition JSON is specifying a condition for the `Status` field in the `Opportunities` dataset. Here's a breakdown of what this means in simple business terms:

- **Target Field**: The filter is applied to the `Status` of opportunities, which typically indicates the current state of a sales opportunity (e.g., whether it's open, closed, won, lost, etc.).

- **Filter Condition**: The filter condition is "`Status` IN ('Open')". This means that we are only interested in opportunities that have a status of "Open".

- **Data Included**: When this filter is applied, only those opportunities that are currently marked as "Open" will be included in any reports or analyses. 

- **Data Excluded**: Any opportunities that have a status other than "Open" (such as "Closed", "Won", "Lost", etc.) will be excluded from the results.

In summary, this filter is used to focus on active sales opportunities that are still in progress, allowing users to analyze or report only on those that are currently open.)
- Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are focusing on the data related to the managers of the owners in your dataset.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `Owners.Manager` field. Instead, it means that **all managers** will be included in the data being analyzed or displayed.

3. **Inclusion of Data**: Since the filter is set to include "(All values)", every manager in the dataset will be considered. This means that regardless of which manager is associated with the owners, all of them will be shown in the report or analysis.

4. **Exclusion of Data**: There are no exclusions in this filter. It does not filter out any managers; therefore, no data related to any manager is omitted.

### Summary:
In summary, this filter allows you to see data for **all managers** without any restrictions. It ensures that every manager's data is included in your analysis, providing a comprehensive view of the performance or metrics associated with all managers in the dataset.)
- Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Owner`. This means we are focusing on the data related to the owners in your dataset.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied**. Instead, it includes **all possible values** for the `Owners.Owner` field.

3. **Data Inclusion**: Since the filter is set to include all values, every owner in your dataset will be considered. This means that when you look at reports or visualizations, you will see data related to every owner without any exclusions.

4. **Use Case**: This type of filter is useful when you want to analyze the overall performance or characteristics of all owners without narrowing down to specific ones. For example, if you want to see total sales, average performance, or any other metric across all owners, this filter ensures that you are looking at the complete picture.

### Summary:
In summary, the filter "(All values)" applied to `Owners.Owner` means that all owners are included in your analysis, and no data is excluded. This allows for a comprehensive view of all owner-related data in your Power BI reports.)
- Filter on `Opportunities`.`Opportunity Owner Name` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Opportunity Owner Name`. This field typically contains the names of individuals or teams responsible for managing sales opportunities.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `Opportunity Owner Name`. This means that all opportunity owners will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter is set to include "(All values)", every opportunity, regardless of who the owner is, will be shown in the report. There are no exclusions based on the owner’s name.

### Summary:
In simple terms, this filter allows you to see all opportunities managed by all owners without any restrictions. It ensures that every opportunity is considered in your analysis, providing a complete view of the data related to opportunity ownership.)
- Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are focusing on the data related to the managers of the owners in your dataset.

2. **Filter Type**: The filter is set to "(All values)". This indicates that no specific restrictions are being applied to the data. 

3. **Data Inclusion**: By using "(All values)", the filter includes every possible value for the `Owners.Manager` field. This means that all managers, regardless of their specific names or characteristics, will be included in the analysis.

4. **Data Exclusion**: Since the filter is set to include all values, there are no exclusions. Every manager's data will be visible in the report or dashboard.

### Summary:

In simple terms, this filter means that when you look at the data related to `Owners.Manager`, you will see information for every manager without any limitations or exclusions. All managers are included in the analysis, allowing for a comprehensive view of the data related to them.)
- Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Products.Product`. This means that no specific criteria are being applied to limit the data.

2. **Data Included**: When this filter is applied, every single product in the `Products` dataset will be included in the report or visualization. There are no exclusions or restrictions.

3. **Business Impact**: This is useful when you want to see a complete overview of all products without filtering out any specific items. For example, if you are analyzing sales data, you would see sales figures for every product available, allowing for a comprehensive analysis.

4. **No Exclusions**: Since the filter is set to "(All values)", there are no products being excluded from the analysis. This ensures that all products are represented in the data being analyzed.

### Summary:
In summary, this filter allows you to view and analyze all products in your dataset without any limitations, providing a full picture of your product data.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when you apply this filter, you are not excluding any categories of products. Every product category available in your dataset will be shown in your report.

2. **Data Inclusion**: Since the filter is set to "(All values)", it ensures that all product categories—such as Electronics, Clothing, Home Goods, etc.—are included in any analysis or visualizations. No categories are filtered out.

3. **Impact on Reporting**: By using this filter, you can see a complete view of your product categories without any restrictions. This is useful when you want to analyze overall trends, performance, or comparisons across all product categories.

### Summary:
In summary, this filter allows you to view and analyze data for every product category without excluding any, providing a comprehensive perspective on your product offerings.)
- Filter on `Industries`.`Industry` (Type: Categorical, Explanation: In simple business terms, this Power BI filter is designed to exclude certain data from the analysis. Specifically, it is applied to the `Industries`.`Industry` field.

Here's what the filter means:

- **`NOT`**: This indicates that we are excluding certain values from our data set.
- **`(`Industry` IN ('n/a'))`**: This part specifies the condition we are looking at. It checks if the value of `Industry` is 'n/a'.

Putting it all together, this filter means:

- **Include all industries except those that are labeled as 'n/a'**. 

In other words, when this filter is applied, any data entries where the industry is marked as 'n/a' will be left out of the analysis. This helps ensure that the analysis focuses only on valid industry data, providing a clearer and more accurate picture of the industries being examined.)

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
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter defined. In simple business terms, this means that when this filter is applied, it does not include or exclude any data. Essentially, it acts as if there is no filter at all.

In practical terms, if you were to use this filter in a Power BI report or dashboard, all data would be displayed without any restrictions. There would be no criteria limiting the data shown, so users would see the complete dataset available in that context.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter definition applied in this context. In simple business terms, this means that there are no criteria set to include or exclude any data when this filter is applied.

### What This Means:
- **No Data Restrictions**: Since there is no filter defined, all data will be included in any analysis or report. There are no limits or conditions that would narrow down the dataset.
- **Full Visibility**: Users will see the complete dataset without any modifications or exclusions, allowing for a comprehensive view of all available information.

In summary, this filter does not change or limit the data in any way; it simply allows everything to be displayed as is.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter definition applied. In simple business terms, this means that there are no criteria set to include or exclude any data when this filter is used.

### What This Means for Your Data:
- **No Data Restrictions**: Since there are no filters defined, all data will be included in any analysis or report. You will see every record available in the dataset without any limitations.
- **Full Visibility**: You can view all the information without any focus on specific segments or categories. This is useful if you want a comprehensive overview of the data.

### Summary:
In essence, this filter does not limit or modify the data in any way, allowing you to see everything in its entirety.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter definition applied in this instance. In simple business terms, this means that there are no criteria set to include or exclude any data when this filter is applied.

### What This Means for Your Data:
- **No Data Restrictions**: Since there are no filters defined, all data will be included in any reports or visualizations. This means you will see the complete dataset without any limitations.
- **Full Visibility**: You can analyze all available information without any specific focus or exclusion of certain data points.

In summary, this filter does not limit or modify the data in any way, allowing you to view everything in its entirety.)
  - Filter on `Opportunities`.`OpportunitySeq` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Opportunities.OpportunitySeq`. This means that no specific criteria are being applied to limit the data.

2. **Data Included**: When this filter is applied, every single opportunity in the dataset will be included in the analysis. There are no exclusions or restrictions based on any conditions.

3. **Impact on Reporting**: Since all opportunities are included, any visualizations, calculations, or insights derived from this data will reflect the complete set of opportunities available, without filtering out any specific ones.

### Summary:
In simple terms, this filter allows you to see everything related to opportunities, without leaving anything out. It ensures that your analysis encompasses the entire dataset for `OpportunitySeq`, providing a comprehensive view of all opportunities.)

**Pipeline by Top Industries**

- Type: `ribbonChart`
- Name: `6fe682ad2620c1cefca0`
- Fields Used:
  - `YEAR MONTH` (Query: `Opportunity Calendar.YEAR MONTH`) (Role: Category)
  - `Revenue Open` (Query: `Opportunities.Revenue Open`) (Role: Y)
  - `Industry` (Query: `Industries.Industry`) (Role: Series)
- Visual Level Filters:
  - Filter on `Accounts`.`Account Name` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all possible values** for the field `Accounts`.`Account Name`. This means that no specific criteria are applied to limit the data shown.

2. **Data Included**: When this filter is applied, every account name from the `Accounts` table will be included in the report or visualization. There are no exclusions, so all accounts will be visible.

3. **Data Excluded**: Since the filter is set to include all values, there are no account names being excluded. Every account that exists in the dataset will be part of the analysis.

### Summary:
In simple terms, this filter allows you to see every account name without any restrictions. It ensures that all accounts are represented in your report, providing a complete view of the data related to account names.)
  - Filter on `Opportunities`.`[Close %]` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field it is applied to, which in this case is `Opportunities.[Close %]`. 

2. **Data Included**: This means that every possible percentage value for the `Close %` field will be considered. There are no restrictions or exclusions, so all opportunities, regardless of their close percentage, will be shown in the report.

3. **No Exclusions**: Since the filter is set to "(All values)", it does not exclude any opportunities based on their close percentage. Whether an opportunity has a close percentage of 0%, 50%, 100%, or any other value, it will be included in the analysis.

### Summary:
When this filter is applied to `Opportunities.[Close %]`, it ensures that all opportunities are visible in the report, allowing for a comprehensive view of the data without any filtering based on the close percentage.)
  - Filter on `Industries`.`Industry` (Type: TopN, Explanation: The provided filter definition JSON, which reads "`Industry` IN ()", is a way to specify which industries should be included in a Power BI report or visualization. 

In simple business terms, this filter is saying:

- **Target Field**: The filter is applied to the `Industry` field in your data model.
- **Condition**: The condition is looking for industries that are included in a list. However, the parentheses are empty, meaning there are no industries specified.

### What This Means:
- **No Industries Included**: Since the list is empty, this filter effectively excludes all industries. In other words, when this filter is applied, no data related to any industry will be shown in the report or visualization.
- **Result**: You will see no results or data points related to industries because the filter does not allow any industries to be included.

### Summary:
This filter is set up to show no data for the `Industry` field because it does not specify any industries to include.)

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

- Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Decision Maker Identified` within the `Opportunities` dataset. This field likely indicates whether a decision maker has been identified for a particular opportunity.

2. **Filter Meaning**: The filter `(All values)` means that **no restrictions** are being applied to the `Decision Maker Identified` field. In other words, all possible values in this field will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter includes all values, it means that:
   - Opportunities where a decision maker **has been identified** will be shown.
   - Opportunities where a decision maker **has not been identified** will also be shown.
   - Essentially, every opportunity, regardless of whether a decision maker is identified or not, will be part of the report.

### Summary:
This filter allows you to see the complete picture of all opportunities, without filtering out any based on whether a decision maker has been identified. It ensures that your analysis includes every opportunity, providing a comprehensive view of the data.)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Context**: The filter is applied to the `Opportunities` table, specifically focusing on the `Purchase Process` field.

2. **What It Means**: The filter `"(All values)"` indicates that **all possible values** in the `Purchase Process` field will be included in the analysis. This means that no specific criteria are being applied to limit or exclude any data.

3. **Data Inclusion**: Since the filter includes all values, every opportunity, regardless of its stage in the purchase process (e.g., prospecting, negotiation, closed-won, closed-lost), will be considered in the report. 

4. **No Exclusions**: There are no exclusions or restrictions placed on the data. This allows for a comprehensive view of all opportunities, providing a complete picture of the purchase processes currently in play.

### Summary:
In summary, applying this filter means you will see all opportunities in the `Purchase Process` without any limitations, allowing for a full analysis of the data related to all stages of the purchase process.)
- Filter on `Industries`.`Industry` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: This filter is set to include **all values** for the field `Industries.Industry`. 

2. **Data Inclusion**: When this filter is applied, it means that no specific industries are being excluded. Instead, every industry in your dataset will be shown in the report or visualization. 

3. **Practical Impact**: If you were looking at a report that analyzes sales by industry, applying this filter would allow you to see sales data for every industry available in your dataset, rather than limiting the view to just a few selected industries.

### Summary:
In simple terms, this filter ensures that all industries are included in the analysis, providing a comprehensive view without any restrictions.)
- Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are focusing on the data related to the managers of owners in your dataset.

2. **Filter Type**: The filter is set to "(All values)". This indicates that there are no restrictions on the data being displayed for the `Owners.Manager` field.

3. **Data Inclusion**: By using "(All values)", the filter includes every possible manager in the dataset. This means that all managers, regardless of any specific criteria (like performance, department, or any other attributes), will be shown in the report.

4. **No Exclusions**: Since the filter is set to include all values, there are no exclusions. Every manager will be represented in the data visualizations, allowing for a comprehensive view of all managers without filtering any out.

### Summary:

In summary, this filter allows you to see data related to all managers in the `Owners` dataset without excluding any specific managers. It provides a complete overview of all managers, ensuring that no relevant data is left out.)
- Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Owner`. This means we are focusing on the data related to the owners of certain items, products, or assets in your dataset.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `Owners.Owner` field. This means that all owners will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter is set to include "(All values)", every owner in the dataset will be considered. There are no restrictions or exclusions based on owner names or categories.

### Summary:
When this filter is applied, you will see data for **all owners** without any limitations. This is useful when you want a comprehensive view of all the owners in your analysis, rather than focusing on a specific subset.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when you apply this filter, you are not excluding any categories of products. 

2. **Data Included**: Every single product category available in your dataset will be shown. For example, if your dataset includes categories like "Electronics," "Clothing," "Home Goods," etc., all of these categories will be included in your report.

3. **Data Excluded**: There are no exclusions with this filter. No product categories will be left out or filtered out from the view.

### Summary:
Using this filter means you will see a complete view of all product categories in your reports, allowing for a comprehensive analysis without any restrictions on which categories are displayed.)
- Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Products`.`Product`. This means that no specific products are being excluded or included; rather, every product in the dataset will be considered.

2. **Data Inclusion**: When this filter is applied, it ensures that all products available in the dataset are shown in the report or visualization. There are no restrictions or limitations on which products can be viewed.

3. **Practical Implication**: If you are looking at sales data, for example, using this filter would allow you to see sales figures for every product, rather than just a subset. This is useful when you want a comprehensive view of all products without any filtering.

### Summary:
The filter `(All values)` means that all products will be included in the analysis, allowing for a complete overview of the data related to products without any exclusions.)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Context**: The filter is applied to the `Opportunities` table, specifically focusing on the `Purchase Process` field.

2. **What It Means**: The filter `"(All values)"` indicates that **all possible values** in the `Purchase Process` field will be included in the analysis. This means that no specific criteria are being applied to limit the data; instead, every opportunity, regardless of its purchase process stage, will be considered.

3. **Data Inclusion**: Since the filter includes all values, it does not exclude any opportunities based on their purchase process status. For example, whether an opportunity is in the "Initial Contact," "Proposal," or "Closed" stage, all of these will be shown in the report.

### Summary:
In summary, this filter allows you to see a complete view of all opportunities in the `Purchase Process`, without filtering out any specific stages or statuses. This is useful when you want to analyze the entire pipeline without any restrictions.)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: The provided filter definition JSON is used to specify which data should be included when analyzing the `Status` of opportunities in Power BI. 

In simple business terms, this filter is saying:

- **Include Only**: The filter is set to include only those opportunities that have a status of "Won." 

This means that when this filter is applied, any opportunities that are not marked as "Won" (such as "Lost," "Pending," or any other status) will be excluded from the analysis. 

In summary, this filter helps focus the analysis specifically on successful opportunities, allowing users to see only the data related to deals that have been successfully closed.)
- Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Decision Maker Identified` within the `Opportunities` dataset. This field likely indicates whether a decision maker has been identified for a particular opportunity.

2. **Filter Meaning**: The phrase "(All values)" means that the filter is not restricting or limiting the data in any way. It is essentially saying, "Include everything." 

3. **Data Included**: When this filter is applied, all records from the `Opportunities` dataset will be included in the analysis, regardless of whether a decision maker has been identified or not. This means you will see opportunities with:
   - Decision makers identified (Yes)
   - Decision makers not identified (No)
   - Any other possible values that might exist in that field.

4. **No Exclusions**: Since the filter specifies "(All values)", there are no exclusions. Every opportunity will be considered, allowing for a comprehensive view of the data.

### Summary:
In summary, applying this filter means you are looking at all opportunities without any restrictions based on whether a decision maker has been identified. This is useful for getting a complete picture of your opportunities, regardless of the status of decision maker identification.)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Context**: The filter is applied to the `Opportunities` table, specifically focusing on the `Purchase Process` field.

2. **What It Means**: The filter `(All values)` indicates that **all possible values** for the `Purchase Process` field are included in the data being analyzed. 

3. **Data Inclusion**: This means that no specific criteria are being applied to limit the data. Every opportunity, regardless of its purchase process stage (like "Initial Contact," "Proposal," "Negotiation," etc.), will be included in the analysis.

4. **No Exclusions**: Since the filter is set to include all values, there are no exclusions. Every opportunity will be considered, allowing for a comprehensive view of all purchase processes.

### Summary:
In summary, this filter ensures that when you look at the `Opportunities` data, you see everything related to the `Purchase Process` without any restrictions. This is useful for getting a complete picture of all opportunities in the sales pipeline.)
- Filter on `Industries`.`Industry` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: This filter is set to include **all values** from the `Industries`.`Industry` field. There are no restrictions or exclusions applied.

2. **Data Included**: When this filter is applied, every industry available in the dataset will be shown. For example, if your dataset includes industries like "Technology," "Healthcare," "Finance," and "Retail," all of these industries will be included in the report.

3. **Data Excluded**: Since the filter is set to include all values, no industries are excluded. This means that you will not miss any data related to any industry in your analysis.

### Summary:
In simple terms, this filter allows you to see data from every industry without any limitations. It ensures that all industries are represented in your Power BI reports, providing a complete view of the data related to industries.)
- Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are focusing on the data related to the managers of owners in your dataset.

2. **Filter Type**: The filter is set to "(All values)". This indicates that no specific restrictions are being applied to the data. 

3. **Data Inclusion**: By using "(All values)", the filter includes every possible value for the `Owners.Manager` field. This means that all managers, regardless of their specific names or attributes, will be included in the analysis.

4. **Data Exclusion**: Since the filter is set to include all values, there are no exclusions. Every manager's data will be visible in the report or dashboard.

### Summary:

In simple terms, this filter means that when you look at the data related to `Owners.Manager`, you will see information for every manager without any limitations. All managers are included, and none are left out. This is useful when you want a complete view of all managers in your analysis.)
- Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Owner`. This means we are focusing on the data related to the owners in your dataset.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied**. This means that all owners will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter is set to include all values, every owner in the dataset will be considered. There are no exclusions or limitations on which owners are shown.

### Summary:
When this filter is applied to the `Owners.Owner` field, it ensures that all owners are included in the report or visualization, allowing you to see the complete picture without any restrictions on the data related to owners.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when you apply this filter, you are not excluding any categories of products. 

2. **Data Included**: Every single product category available in your dataset will be shown. For example, if your product categories include "Electronics," "Clothing," "Home Goods," and "Toys," all of these categories will be included in the report.

3. **Data Excluded**: There are no exclusions with this filter. No product categories are left out; everything is visible.

### Summary:
Using this filter means you want to see a complete view of all product categories without any restrictions. This is useful when you want to analyze overall performance or trends across all categories without focusing on a specific subset.)
- Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: This filter is set to include **all possible values** for the target field, which in this case is `Products`.`Product`. 

2. **Data Included**: When this filter is applied, it means that every single product in your dataset will be shown. No products are excluded; all products are considered for any analysis or visualizations.

3. **Use Case**: This is useful when you want to see a complete overview of all products without any restrictions. For example, if you are analyzing sales data and want to see how each product is performing, using this filter ensures that you are looking at the entire product range.

4. **No Exclusions**: Since the filter is set to "(All values)", there are no exclusions. You won't miss any products, regardless of their sales performance or any other criteria.

### Summary:
In summary, this filter allows you to view and analyze **every product** in your dataset without any limitations, ensuring a comprehensive understanding of your product offerings.)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: This filter is set to include **all possible values** for the field it is applied to, which in this case is the `Purchase Process` within the `Opportunities` dataset.

2. **Data Inclusion**: By using "(All values)", the filter does not exclude any records. This means that every opportunity, regardless of its purchase process stage (e.g., Lead, Proposal, Negotiation, Closed Won, Closed Lost), will be included in the analysis.

3. **No Restrictions**: There are no restrictions or conditions applied to the data. Essentially, you are looking at the complete picture of all opportunities without filtering out any specific stages or types of purchase processes.

### Summary:
When this filter is applied to the `Opportunities`.`Purchase Process`, it ensures that all opportunities are considered in your analysis, allowing for a comprehensive view of the entire purchase process without any exclusions.)

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
  - Filter on (Name: `Filter9eafa29b773622144b40`) (Type: Exclude, Explanation: In simple business terms, this Power BI filter definition is saying:

**"Exclude any data where the 'Campaign' field is equal to 'null'."**

Here's a breakdown of what this means:

- **Campaign**: This refers to a specific field or column in your dataset that likely contains information about marketing campaigns or similar initiatives.
  
- **IN ('null')**: This part is checking if the value in the 'Campaign' field is 'null'. In data terms, 'null' typically means that there is no value or that the data is missing.

- **NOT**: This indicates that we want to exclude the records that meet the condition specified.

So, when this filter is applied, it will include all records where the 'Campaign' field has a value (i.e., it is not 'null') and will exclude any records where the 'Campaign' field does not have a value. Essentially, you will only see data related to campaigns that have been defined or specified, and any records without a campaign will be left out of your analysis.)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: In simple business terms, this Power BI filter is designed to include only those opportunities that do **not** have a status of "Lost." 

Here's a breakdown of what this means:

- **Target Field**: The filter is applied to the `Status` field of the `Opportunities` data.
- **Condition**: The filter specifically looks for opportunities where the status is **not** in the list of statuses that include "Lost."
- **Result**: When this filter is applied, any opportunity that has been marked as "Lost" will be excluded from the data being analyzed or displayed. Only opportunities with other statuses (like "Open," "Won," etc.) will be included.

In summary, this filter helps focus on opportunities that are still viable or active, by filtering out those that have already been lost.)
- Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Decision Maker Identified` within the `Opportunities` dataset. This field likely indicates whether a decision maker has been identified for a particular opportunity.

2. **Filter Meaning**: The filter value of `"(All values)"` means that **no restrictions** are being applied to the `Decision Maker Identified` field. 

3. **Data Included**: When this filter is active, it includes **all records** from the `Opportunities` dataset, regardless of whether a decision maker has been identified or not. This means you will see opportunities where:
   - A decision maker is identified.
   - No decision maker is identified.

4. **Business Impact**: By using this filter, you ensure that your analysis or report reflects the complete picture of all opportunities, allowing stakeholders to see both those with identified decision makers and those without. This can be crucial for understanding the overall pipeline and making informed business decisions.

In summary, the filter `"(All values)"` allows you to view every opportunity in your dataset without excluding any based on whether a decision maker has been identified.)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Context**: The filter is applied to the `Opportunities`.`Purchase Process` data. This means we are looking at the specific aspect of the sales process related to opportunities for purchases.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied**. Instead, it includes **all possible values** for the `Purchase Process` field. 

3. **Data Inclusion**: Because the filter is set to include all values, every opportunity in the dataset will be considered, regardless of its stage or status in the purchase process. This means that all opportunities—whether they are in the initial stages, negotiation, or closed—will be shown in the report.

4. **Data Exclusion**: There are no exclusions with this filter. Since it encompasses all values, no opportunities are left out based on the `Purchase Process`.

### Summary:
In summary, this filter allows you to see every opportunity in the purchase process without any restrictions. It provides a complete view of all opportunities, helping you analyze the entire pipeline without missing any data points.)
- Filter on `Industries`.`Industry` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Industries.Industry`. This means that no specific industries are being excluded or included; rather, every industry available in the dataset will be shown.

2. **Data Impact**: When this filter is applied, it ensures that all industries are represented in the report or visualization. For example, if your dataset includes industries like Technology, Healthcare, Finance, and Retail, all of these will be visible and considered in any analysis or visualizations.

3. **Use Case**: This type of filter is useful when you want to see a comprehensive view of all industries without any restrictions. It allows stakeholders to analyze trends, performance, or other metrics across the entire range of industries available in the data.

### Summary:
In summary, the filter definition `(All values)` means that the report will display data for every industry without any exclusions, providing a complete overview of the industry landscape in your analysis.)
- Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are focusing on the data related to the managers of owners in your dataset.

2. **Filter Type**: The filter is set to "(All values)". This indicates that no specific restrictions are being placed on the data. 

3. **Data Inclusion**: By using "(All values)", the filter includes every possible value for the `Owners.Manager` field. This means that all managers, regardless of their specific names or attributes, will be included in the analysis.

4. **Data Exclusion**: Since the filter is set to include all values, there are no exclusions. Every manager in the dataset will be considered, and none will be left out.

### Summary:
In simple terms, this filter means that when you look at the data related to `Owners.Manager`, you will see information for every manager without any limitations or exclusions. All managers are included in the report or visualization, allowing for a comprehensive view of the data.)
- Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Owner`. This means we are focusing on the data related to the owners of certain items, products, or assets in your dataset.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `Owners.Owner` field. This means that all owners will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter is set to "(All values)", every owner in the dataset will be considered. There are no exclusions or restrictions on which owners are shown.

### Summary:
When this filter is applied, you will see data for **every owner** in your dataset without any limitations. This is useful when you want a comprehensive view of all owners and their associated data, rather than focusing on a specific subset.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when you apply this filter, you are not excluding any categories of products. Every product category available in your dataset will be shown in your reports.

2. **Data Inclusion**: Since the filter is set to "(All values)", it ensures that all product categories—such as Electronics, Clothing, Home Goods, etc.—are included in the analysis. No categories are filtered out, so you will see a complete view of all products.

3. **Impact on Reporting**: By using this filter, you can analyze overall trends, performance, and insights across all product categories without any restrictions. This is useful when you want to get a comprehensive understanding of your product offerings and how they perform collectively.

### Summary:
In summary, this filter allows you to see **everything** related to product categories in your Power BI report, ensuring that no data is left out.)
- Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Products.Product`. This means that no specific criteria are being applied to limit the data.

2. **Data Included**: When this filter is applied, every single product in the `Products` table will be included in the report or visualization. There are no exclusions; all products, regardless of their attributes (like category, price, availability, etc.), will be shown.

3. **Data Excluded**: Since the filter is set to include all values, there are no products being excluded. Every product that exists in the dataset will be part of the analysis.

### Summary:
In simple terms, this filter allows you to see **everything** related to products without any restrictions. It’s like saying, "Show me all the products we have, without leaving anything out.")
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Opportunities.Purchase Process`. This means that no specific criteria are applied to limit the data shown.

2. **Data Included**: When this filter is applied, every single entry in the `Purchase Process` field of the `Opportunities` dataset will be included in the report. This could encompass all stages of the purchase process, such as "Lead", "Proposal", "Negotiation", "Closed Won", "Closed Lost", etc.

3. **Data Excluded**: Since the filter is set to include all values, there are no exclusions. No data related to the `Purchase Process` will be left out; everything is considered.

### Summary:
In simple terms, this filter allows you to see all opportunities regardless of their purchase process stage. It does not restrict or filter out any specific stages, ensuring a comprehensive view of all opportunities in the dataset.)

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
  - Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the `Opportunities`.`Status` field. This field typically represents the current state of various business opportunities, such as "Open," "Closed Won," "Closed Lost," etc.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `Status` field. This means that all possible statuses of opportunities will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter includes all values, every opportunity, regardless of its status, will be considered. For example, if you have opportunities that are "Open," "Closed Won," and "Closed Lost," all of these will be shown in your report.

4. **Data Exclusion**: There are no exclusions with this filter. No opportunities are being left out based on their status.

### Summary:
In summary, this filter allows you to see **all opportunities** in your report, regardless of their status. It does not limit the data in any way, ensuring a comprehensive view of all opportunities available in the dataset.)
  - Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: This filter is set to include **all possible values** for the target field, which in this case is `Products`.`Product`. 

2. **Data Inclusion**: When this filter is applied, it means that every single product in the dataset will be shown. There are no restrictions or exclusions; all products are included in the analysis.

3. **No Exclusions**: Since the filter specifies "(All values)", it does not exclude any products. This is useful when you want to see a complete overview of all products without any limitations.

### Practical Implication:

- If you are creating a report that shows sales data, applying this filter will allow you to see sales figures for every product in your inventory. You won't miss out on any products, and you can analyze the performance of your entire product range.

In summary, this filter ensures that all products are visible in your Power BI report, providing a comprehensive view of your product data.)
  - Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when this filter is applied, no categories are excluded from the data being analyzed or displayed.

2. **Data Included**: Every single product category in your dataset will be shown. For example, if your product categories include "Electronics," "Clothing," "Home Goods," and "Toys," all of these categories will be included in the report.

3. **Data Excluded**: There are no exclusions. Since the filter is set to "(All values)," it does not filter out any categories, so you will see a complete view of all product categories available in your data.

### Summary:
When you apply this filter to the `Products`.`Product Category`, you are ensuring that every product category is visible in your reports, allowing for a comprehensive analysis without any restrictions on the data being displayed.)
  - Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Owner`. This means we are focusing on the data related to the owners of certain items, products, or assets in your dataset.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `Owners.Owner` field. Instead, it includes **all possible owners** in the dataset.

3. **Data Inclusion**: When this filter is applied, every owner in the dataset will be included in the report or visualization. There are no restrictions or exclusions based on owner names or categories.

4. **Business Impact**: This means that if you are analyzing sales, inventory, or any other metrics related to ownership, you will see data for every owner without any limitations. This is useful when you want a comprehensive view of all owners and their associated data.

### Summary:
In summary, the filter "(All values)" ensures that all owners are included in your analysis, allowing you to see the complete picture without omitting any specific owner from the data.)
  - Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are focusing on the data related to the managers of owners in your dataset.

2. **Filter Type**: The filter is set to "(All values)". This indicates that no specific restrictions are being applied to the data. 

3. **Data Inclusion**: By using "(All values)", the filter includes every possible manager in the dataset. This means that all managers, regardless of any specific criteria or conditions, will be considered in the analysis.

4. **Data Exclusion**: Since the filter is set to include all values, there are no exclusions. Every manager's data will be visible in the report.

### Summary:

In simple terms, this filter means that when you look at the data related to `Owners.Manager`, you will see information for every manager without any limitations or exclusions. All managers are included in the analysis, allowing for a comprehensive view of the data related to them.)
  - Filter on `Industries`.`Industry` (Type: Categorical, Explanation: The filter definition JSON you provided, `"(All values)"`, indicates that no specific filtering is being applied to the target field `Industries.Industry`. 

In simple business terms, this means that when this filter is applied, all industries will be included in the data analysis or report. There are no restrictions or exclusions, so every industry in the dataset will be considered. 

In summary, this filter allows you to see data from every industry without any limitations.)
  - Filter on `Accounts`.`State or Province` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: This filter is set to include **all possible values** for the field `Accounts`.`State or Province`. 

2. **Data Included**: When this filter is applied, it does not exclude any states or provinces. This means that every state or province in your dataset will be considered and displayed in your reports.

3. **Data Excluded**: Since the filter is set to include all values, there are no exclusions. No states or provinces will be left out of the analysis.

### Summary:
In simple terms, this filter allows you to see data from every state or province in your accounts, ensuring that no location is omitted from your analysis. This is useful when you want a comprehensive view of your data across all regions.)
  - Filter on `Territories`.`Region` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Territories.Region` field. This means that when this filter is applied, it does not exclude any regions from the data being analyzed or displayed.

2. **Data Inclusion**: Since the filter is set to "(All values)", every region in the `Territories` dataset will be included in the report. For example, if your dataset includes regions like North, South, East, and West, all of these regions will be shown in your visualizations.

3. **No Exclusions**: There are no restrictions or exclusions applied to the data. This is useful when you want to see a complete overview of all regions without filtering out any specific ones.

### Summary:
In summary, this filter ensures that all regions from the `Territories` dataset are included in your analysis, allowing for a comprehensive view of the data without any limitations.)
  - Filter on `Territories`.`Territory` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Territories.Territory`. This means that no specific territories are being excluded or included; instead, every territory in the dataset will be considered.

2. **Data Impact**: When this filter is applied, it ensures that all territories are visible in your reports. For example, if you have territories like "North", "South", "East", and "West", all of these will be shown in your analysis without any restrictions.

3. **Use Case**: This type of filter is useful when you want to see a complete overview of all territories without narrowing down to specific ones. It allows for a comprehensive analysis of data across all regions.

### Summary:
In summary, the filter `(All values)` means that when analyzing the `Territories.Territory`, you will see data from every territory available in your dataset, providing a full picture without any exclusions.)
  - Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Opportunities.Purchase Process`. This means that no specific criteria are being applied to limit the data shown.

2. **Data Included**: When this filter is applied, every opportunity in the dataset will be considered, regardless of its purchase process stage. This includes all stages such as "Lead," "Proposal," "Negotiation," "Closed Won," and "Closed Lost," or any other stages defined in your data.

3. **Data Excluded**: Since the filter is set to include all values, there are no exclusions. Every opportunity will be visible in the report or dashboard.

### Summary:
In summary, applying this filter means you will see a complete view of all opportunities in the purchase process without any restrictions. This is useful when you want to analyze the entire dataset without focusing on specific stages or criteria.)
  - Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Decision Maker Identified` within the `Opportunities` dataset. This field likely indicates whether a decision maker has been identified for a particular opportunity.

2. **Filter Type**: The filter is set to "(All values)". This means that no specific criteria are being applied to the `Decision Maker Identified` field.

3. **Data Inclusion**: Since the filter includes all values, it means that every opportunity, regardless of whether a decision maker has been identified or not, will be included in the report. 

4. **No Exclusions**: There are no exclusions in this filter. Opportunities with a decision maker identified and those without will both be shown.

### Summary:
In simple terms, this filter allows you to see all opportunities in your report, without filtering out any based on whether a decision maker has been identified. It provides a complete view of the data related to opportunities.)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: In simple business terms, this Power BI filter definition is specifying which opportunities should be included in the analysis based on their status.

Here's what it means:

- The filter is applied to the `Status` field of the `Opportunities` data.
- It includes only those opportunities that have a status of either **'Open'** or **'Won'**.

So, when this filter is applied, any opportunities that are marked as **'Closed'**, **'Lost'**, or any other status not listed will be excluded from the analysis. Essentially, you are focusing on opportunities that are currently active (Open) or have been successfully completed (Won).)
- Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to control which data is included in the analysis based on the `RELATIVE MONTH` field from the `Opportunity Calendar`. Let's break it down in simple business terms:

1. **`RELATIVE MONTH` > -6**: This part of the filter is saying that we want to include only those records where the `RELATIVE MONTH` value is greater than -6. In practical terms, this means we are looking at opportunities that occurred in the last 6 months and any future months. For example, if today is October 2023, this filter will include data from April 2023 onward.

2. **NOT (`RELATIVE MONTH` = null)**: This part of the filter ensures that we do not include any records where the `RELATIVE MONTH` value is missing or undefined (i.e., null). In business terms, it means we want to exclude any opportunities that do not have a valid month associated with them.

### Summary:
When this filter is applied, it will include only those opportunities that have a `RELATIVE MONTH` value indicating they are from the last 6 months or any future month, while also excluding any records that do not have a specified month. This helps in focusing the analysis on relevant and timely opportunities.)
- Filter on `Opportunities`.`Sales Stage` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the `Sales Stage` field within the `Opportunities` dataset. This field typically represents different stages in the sales process, such as "Prospecting," "Negotiation," "Closed Won," etc.

2. **Filter Action**: The filter is set to include **all values** from the `Sales Stage` field. This means that when this filter is applied, it does not exclude any sales stages. 

3. **Data Impact**: As a result, every opportunity, regardless of its sales stage, will be included in the report or visualization. You will see data for all opportunities, whether they are at the beginning of the sales process or have already been closed.

### Summary:
In simple terms, this filter ensures that you are looking at the complete picture of your sales opportunities by including every stage of the sales process. No opportunities are left out, allowing for a comprehensive analysis of all sales activities.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when this filter is applied, it does not exclude any categories of products. 

2. **Data Included**: Every single product category available in the dataset will be shown. For example, if your product categories include "Electronics," "Clothing," "Home Goods," and "Toys," all of these categories will be included in the report.

3. **Data Excluded**: There are no exclusions with this filter. No product categories are left out, so you will see a complete view of all product categories.

### Summary:
When you apply this filter to the `Products`.`Product Category`, you are ensuring that all product categories are visible in your report, allowing for a comprehensive analysis of all products without any restrictions.)
- Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Owner`. This means we are focusing on the data related to the owners in your dataset.

2. **Filter Type**: The filter is set to "(All values)". This indicates that there are no restrictions on the data being displayed for the `Owners.Owner` field.

3. **Data Inclusion**: By using "(All values)", the filter includes every possible owner in the dataset. This means that all owners, regardless of any specific criteria or conditions, will be shown in your reports.

4. **No Exclusions**: Since the filter is set to include all values, there are no owners being excluded from the data. Every owner will be represented in the analysis.

### Summary:
In simple terms, this filter means that when you look at the data for `Owners.Owner`, you will see every owner without any limitations or exclusions. All owners are included in the analysis, allowing for a complete view of the data related to ownership.)
- Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Products`.`Product`. This means that no specific products are being excluded or included; instead, every product in the dataset will be considered.

2. **Data Inclusion**: When this filter is applied, it ensures that all products available in the `Products` table will be shown in your report or visualization. There are no restrictions or conditions limiting which products can be displayed.

3. **Practical Implication**: If you are looking at sales data, for example, this filter allows you to see sales figures for every product without any filtering. It’s useful when you want a comprehensive view of all products rather than focusing on a specific subset.

### Summary:
In summary, the filter definition `"(All values)"` means that all products will be included in your analysis, allowing you to see the complete picture without any exclusions.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when this filter is applied, no categories are excluded from the data being analyzed or displayed.

2. **Data Inclusion**: Every product category available in the dataset will be shown. For example, if your product categories include "Electronics," "Clothing," and "Home Goods," all of these categories will be included in the report.

3. **No Exclusions**: Since the filter specifies "(All values)," there are no restrictions or limitations on the data. This is useful when you want to see a complete overview of all product categories without filtering out any specific ones.

### Summary:
In summary, this filter allows you to view all product categories in your Power BI report, ensuring that no data is left out. It provides a comprehensive view of the entire range of products available in your dataset.)

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
  - Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: In simple business terms, this Power BI filter definition is specifying that we want to focus only on opportunities that are currently in the "Open" status. 

Here's a breakdown of what this means:

- **Target Field**: The filter is applied to the `Status` field of the `Opportunities` data.
- **Included Data**: By using the filter `Status IN ('Open')`, we are including only those opportunities that have their status marked as "Open."
- **Excluded Data**: Any opportunities that have a status other than "Open" (such as "Closed," "Won," "Lost," etc.) will be excluded from the analysis or report.

In summary, this filter helps us narrow down our view to only those opportunities that are still active and available for follow-up or further action, allowing for more focused analysis on current business prospects.)

**Revenue Won and Revenue In Pipeline by Product LOB**

- Type: `barChart`
- Name: `90b98cca54dd8f762bb3`
- Fields Used:
  - `Product Category` (Query: `Products.Product LOB`) (Role: Category)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Y)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Y)
  - `Product` (Query: `Products.Product`) (Role: Category)
- Visual Level Filters:
  - Filter on `Owners`.`[Rev Goal]` (Type: Advanced, Explanation: In simple business terms, the provided Power BI filter definition JSON is specifying a condition that affects how data is displayed for the target field `Owners.[Rev Goal]`.

Here's what it means:

- The filter is checking if the value in the `Rev Goal` field is **not equal to zero**. 
- The notation "`?`" represents the values in the `Rev Goal` field for each owner.
- The condition "`?` <> 0M" means that only those records where the `Rev Goal` is greater than or less than zero will be included in the report or visualization.

### In Summary:
- **Included**: Any owner whose revenue goal is either a positive number or a negative number.
- **Excluded**: Any owner whose revenue goal is exactly zero.

This filter helps to focus on owners who have a defined revenue goal, whether it's a target to achieve (positive) or a deficit (negative), and ignores those who have no goal set at all (zero).)

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
  - Filter on `Owners`.`[Rev Goal]` (Type: Advanced, Explanation: In simple business terms, the provided Power BI filter definition JSON is specifying a condition that affects how data is displayed for the target field `Owners.[Rev Goal]`.

Here's what it means:

- The filter is checking if the value of `Owners.[Rev Goal]` is **not equal to zero** (denoted by `<> 0M`).
- The `M` indicates that the value is in millions, which is a common way to represent large numbers in financial data.

### What this filter does:
- **Includes**: Any records where the `Rev Goal` is greater than zero (i.e., positive revenue goals).
- **Excludes**: Any records where the `Rev Goal` is zero or negative (i.e., no revenue goal or a goal that is a loss).

### Summary:
When this filter is applied, you will only see data for owners who have a revenue goal that is greater than zero. This helps focus on those who are actively aiming to achieve revenue targets, filtering out any owners without a goal or with a goal of zero.)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: The provided filter definition JSON specifies a condition that focuses on the `Status` field of the `Opportunities` data. In simple business terms, this filter is used to include only those opportunities that are currently either "Open" or "Won."

Here's a breakdown of what this means:

- **Included Data**: 
  - **Open**: Opportunities that are still active and have not yet been closed or completed. These are potential sales that are still in progress.
  - **Won**: Opportunities that have been successfully closed and the sale has been completed. These represent successful transactions.

- **Excluded Data**: 
  - Any opportunities that are not "Open" or "Won" will be excluded from the analysis. This typically includes opportunities that are "Lost," "Closed," or in any other status that does not indicate an active or successful sale.

In summary, when this filter is applied, you will only see opportunities that are either still in progress or have been successfully completed, allowing for a focused analysis on current and successful sales efforts.)
- Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to control which data is included in the analysis based on the `RELATIVE MONTH` field from the `Opportunity Calendar`. Let's break it down in simple business terms:

1. **`RELATIVE MONTH` > -6**: This part of the filter means that we are only interested in opportunities that occurred in the last 6 months or more recent. In other words, it includes any data where the `RELATIVE MONTH` value is greater than -6. If `RELATIVE MONTH` is -5, -4, -3, -2, -1, or 0, those months will be included. However, any data older than 6 months (i.e., -7 or lower) will be excluded.

2. **NOT (`RELATIVE MONTH` = null)**: This part of the filter ensures that we do not include any records where the `RELATIVE MONTH` value is missing or undefined (null). This means that if there is no month information available for an opportunity, that record will be excluded from the analysis.

### Summary:
When this filter is applied, it includes only the opportunities from the last 6 months (including the current month) and excludes any records that do not have a specified month. This helps focus the analysis on recent opportunities while ensuring that all data is complete and relevant.)
- Filter on `Opportunities`.`Sales Stage` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the `Sales Stage` field within the `Opportunities` dataset. This field typically represents different stages in the sales process, such as "Prospecting," "Negotiation," "Closed Won," etc.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `Sales Stage`. This means that all possible sales stages will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter includes "All values," every opportunity, regardless of its sales stage, will be considered. This allows you to see a complete picture of all opportunities in the dataset without excluding any stages.

4. **Business Impact**: By applying this filter, you can analyze overall sales performance, trends, or metrics without missing any opportunities that might be at different stages of the sales process. It ensures that your insights are comprehensive and reflect the entire sales pipeline.

### Summary:
In summary, the filter "(All values)" means that when looking at the `Sales Stage` of opportunities, you are including every stage without any exclusions. This provides a full view of all sales opportunities in your analysis.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when this filter is applied, it does not exclude any categories of products. 

2. **Data Included**: Every single product category available in the dataset will be shown. For example, if your dataset includes categories like "Electronics," "Clothing," and "Home Goods," all of these categories will be included in your report.

3. **Data Excluded**: There are no exclusions with this filter. Since it is set to "(All values)," no product categories are filtered out or hidden from view.

### Summary:
When you apply this filter to the `Products`.`Product Category`, you will see all product categories without any restrictions. This is useful when you want a comprehensive view of all categories in your analysis or report.)
- Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Owners.Owner`. This means that no specific owners are being excluded or included; rather, every owner in the dataset will be considered.

2. **Data Inclusion**: When this filter is applied, it ensures that all owners are visible in the report or visualization. There are no restrictions on which owners are shown, so you will see data for every owner present in the dataset.

3. **Practical Implication**: If you were looking at a report that shows sales performance by owner, applying this filter would allow you to see the performance metrics for every single owner without any limitations. You would not miss out on any data related to specific owners.

### Summary:
In summary, the filter `(All values)` means that all owners will be included in the analysis, allowing for a comprehensive view of the data related to every owner in the dataset. There are no exclusions, so you get a complete picture.)
- Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visuals. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Products.Product`. This means that no specific criteria are being applied to limit the data.

2. **Data Included**: When this filter is applied, every single product in the dataset will be included in the report or visual. There are no exclusions, so all products—regardless of their attributes, categories, or any other characteristics—will be shown.

3. **Data Excluded**: Since the filter is set to include all values, there are no products being excluded. Every product that exists in the dataset will be visible.

### Summary:
In simple terms, this filter ensures that all products are displayed without any restrictions. It allows users to see the complete list of products available in the dataset, making it useful for comprehensive analysis or reporting where no specific filtering is desired.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that no specific categories are being excluded or included; instead, every product category available in the dataset will be considered.

2. **Data Inclusion**: When this filter is applied, it ensures that all product categories—such as Electronics, Clothing, Home Goods, etc.—are included in any analysis or visualizations. There are no restrictions on which categories can be shown.

3. **Impact on Reporting**: Because the filter allows for all categories, any report or dashboard that uses this filter will display data from every product category. This is useful when you want a comprehensive view of all products without limiting the analysis to specific categories.

### Summary:
In summary, the filter definition `"(All values)"` means that when analyzing the `Product Category`, you will see data from every category available, providing a complete overview without any exclusions.)

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

- Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to control which data is included when analyzing the `RELATIVE MONTH` field in the `Opportunity Calendar` dataset. Let's break it down in simple terms:

1. **`RELATIVE MONTH`**: This field likely represents a time period relative to the current date. For example, it could indicate months in the past or future, where:
   - `0` represents the current month,
   - `-1` represents the previous month,
   - `-2` represents two months ago, and so on.

2. **Filter Conditions**:
   - **`RELATIVE MONTH > -16`**: This part of the filter means that we are including data from the last 15 months up to the current month. Specifically, it excludes any data that is older than 15 months ago. So, if today is October 2023, this condition would include data from May 2022 (which is -16) onward.
   - **`RELATIVE MONTH >= 0`**: This condition specifies that we are only interested in data from the current month and any future months. It excludes any data from the past months (i.e., it excludes any month with a negative value).

3. **Combined Effect**: When both conditions are applied together, the filter effectively includes data from the current month (0) and the previous 15 months (from -1 to -15), but excludes any data older than 15 months (i.e., anything less than -16). 

### Summary:
In summary, this filter allows you to analyze opportunities from the current month and the previous 15 months, while excluding any opportunities that are older than 15 months. This is useful for focusing on recent and relevant data in your analysis.)
- Filter on `Opportunities`.`Sales Stage` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the `Sales Stage` field within the `Opportunities` dataset. This field typically represents different stages in the sales process, such as "Prospecting," "Negotiation," "Closed Won," or "Closed Lost."

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `Sales Stage`. This means that all possible sales stages will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter is set to include all values, every opportunity, regardless of its sales stage, will be considered. This allows for a comprehensive view of all opportunities in the dataset without excluding any based on their current sales stage.

### Summary:
In simple terms, this filter means that when looking at the `Sales Stage` of opportunities, you will see every opportunity in the dataset, without any restrictions or exclusions based on their sales stage. This is useful for getting a complete picture of all sales activities.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when you apply this filter, you are not excluding any categories of products. 

2. **Data Included**: Every single product category available in your dataset will be shown. For example, if your dataset includes categories like "Electronics," "Clothing," "Home Goods," etc., all of these categories will be included in your report.

3. **Data Excluded**: There are no exclusions with this filter. No product categories are left out; everything is visible.

### Summary:
Using this filter means you want to see a complete view of all product categories without any restrictions. This is useful when you want to analyze overall trends or performance across all categories rather than focusing on specific ones.)
- Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Owners.Owner`. This means that when this filter is applied, it does not restrict or limit the data based on any specific criteria. 

2. **Data Included**: Every single owner from the `Owners` table will be included in the report or visualization. There are no exclusions, so all owners will be visible, regardless of any attributes or conditions.

3. **No Exclusions**: Since the filter is set to "(All values)", there are no owners being filtered out. This is useful when you want to see a complete overview of all owners without any segmentation or filtering.

### Summary:
In summary, this filter ensures that all owners are included in the analysis, providing a comprehensive view without any restrictions.)
- Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Products.Product`. This means that no specific criteria are applied to limit the data shown.

2. **Data Included**: When this filter is applied, every single product in the dataset will be included in the report or visualization. There are no exclusions; all products, regardless of their attributes (like category, price, availability, etc.), will be displayed.

3. **Data Excluded**: Since the filter is set to include all values, there are no products being excluded. Every product that exists in the `Products` table will be visible.

### Summary:
In simple terms, this filter allows you to see **everything** related to products without any restrictions. It’s like saying, "Show me all the products we have, without leaving anything out.")
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the `Product Category` field within the `Products` dataset.

2. **Filter Type**: The filter is set to include **all values**. This means that when this filter is applied, it does not exclude any product categories from the data being analyzed.

3. **Data Inclusion**: Since the filter specifies "(All values)", every product category—regardless of its type, such as electronics, clothing, or furniture—will be included in the report or visualization. 

4. **No Restrictions**: There are no restrictions or limitations on the data shown. This is useful when you want to see a complete overview of all product categories without filtering out any specific ones.

### Summary:
In summary, this filter ensures that all product categories are included in your analysis, allowing you to view the entire range of products without any exclusions.)

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
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: In simple business terms, the provided filter definition JSON is specifying a condition for the data related to the `RELATIVE MONTH` field in the `Opportunity Calendar`. 

Here's what it means:

- **`RELATIVE MONTH`**: This field likely represents a time period in months relative to the current date. For example, `0` could mean the current month, `-1` could mean last month, `-2` could mean two months ago, and so on.

- **`<> -12`**: This part of the filter means "not equal to -12." In this context, `-12` refers to the month that is exactly one year ago from the current month.

### What the Filter Does:
- **Includes**: All data for months that are not equal to one year ago. This means it will include data for the current month, last month, two months ago, and so forth, up to eleven months ago.

- **Excludes**: Any data that corresponds to the month that was exactly one year ago. For example, if today is October 2023, the filter will exclude any data from October 2022.

### Summary:
This filter is used to focus on more recent opportunities by excluding any data from exactly one year ago, allowing analysts to concentrate on the most relevant and timely information.)

**Value In Pipeline**

- Type: `kpi`
- Name: `3562065fddd9c2eb3aa5`
- Fields Used:
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Indicator)
  - `RELATIVE MONTH` (Query: `Opportunity Calendar.RELATIVE MONTH`) (Role: TrendLine)
- Visual Level Filters:
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: In simple business terms, this Power BI filter is designed to include only those records from the `Opportunity Calendar` where the `RELATIVE MONTH` value is not equal to -16.

### Breakdown of the Filter:
- **`RELATIVE MONTH`**: This is a field that likely represents a time period relative to the current date. For example, it could indicate months in the past or future, where:
  - A value of `0` might represent the current month,
  - A value of `-1` would represent the previous month,
  - A value of `-16` would represent 16 months ago.

### What the Filter Does:
- **Includes Data**: The filter allows all records where the `RELATIVE MONTH` is any value **except** -16. This means that any opportunities or data points that occurred 16 months ago will be excluded from the analysis.
  
### Summary:
In essence, when this filter is applied, you will see all opportunities from the `Opportunity Calendar` except those that are dated 16 months back. This helps focus the analysis on more recent opportunities, making it easier to understand current trends and performance without the influence of older data.)

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
  - Filter on `Opportunities`.`[Close %]` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field it is applied to, which in this case is `Opportunities.[Close %]`. 

2. **Data Included**: This means that every opportunity, regardless of its close percentage, will be considered in the analysis. There are no restrictions or exclusions based on the close percentage.

3. **No Exclusions**: Since the filter is set to "All values," it does not exclude any opportunities. Whether an opportunity has a close percentage of 0%, 50%, 100%, or any other value, it will be included in the data being analyzed.

### Summary:
When this filter is applied to `Opportunities.[Close %]`, it ensures that all opportunities are taken into account, allowing for a comprehensive view of the data without any filtering based on the close percentage. This is useful when you want to analyze the overall performance or trends without limiting the data set.)
  - Filter on (Name: `Filterfce64fda3a5931380f90`) (Type: Advanced, Explanation: The JSON you provided indicates that there is no specific filter definition available. In simple business terms, this means that when this filter is applied, it does not include or exclude any specific data. Essentially, it acts as if there are no restrictions on the data being displayed.

In practical terms, if you were to use this filter in a Power BI report, all relevant data would be shown without any limitations. There are no criteria set to narrow down or focus on particular data points, so everything remains visible.)
  - Filter on (Name: `Filterfd148b1dc07e587ec636`) (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter definition applied in this case. In simple business terms, this means that there are no criteria set to include or exclude any data when this filter is used.

### What This Means for Your Data:
- **No Data Restrictions**: Since there are no filters defined, all data will be included in any analysis or report where this filter is applied. 
- **Full Visibility**: You will see all records and values without any limitations or exclusions.
- **Default Behavior**: This is essentially the default state, where no filtering is taking place, allowing for a comprehensive view of the dataset.

In summary, with this filter, you are not filtering out any data; everything is included.)
  - Filter on (Name: `Filter378449185421910ec48c`) (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter defined for the data in question. In simple business terms, this means that when you apply 'this filter', it does not impose any restrictions or criteria on the data being displayed.

### Key Points:
- **No Filters Applied**: Since there is no filter definition, all data will be included in the analysis or report.
- **Complete Data Visibility**: You will see every relevant data point without any exclusions, allowing for a comprehensive view of the dataset.
- **No Specific Criteria**: There are no conditions set to limit or narrow down the data, so everything remains visible.

In summary, this filter does not change or limit the data; it simply allows all available data to be shown.)
  - Filter on `Opportunities`.`OpportunitySeq` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Opportunities.OpportunitySeq`. This means that no specific criteria are being applied to limit the data.

2. **Data Included**: When this filter is applied, every single opportunity in the dataset will be included in the analysis. There are no exclusions or restrictions based on any conditions.

3. **Impact on Reporting**: Since all opportunities are included, any visualizations or calculations based on `OpportunitySeq` will reflect the complete dataset. This is useful when you want to see the overall performance or trends without filtering out any specific opportunities.

### Summary:
In summary, this filter allows you to view all opportunities without any limitations, ensuring that your analysis encompasses the entire dataset related to `OpportunitySeq`.)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: The provided filter definition JSON is used to filter data based on the `RELATIVE MONTH` field in the `Opportunity Calendar`. Let's break it down in simple business terms:

1. **Field Being Filtered**: The filter is applied to the `RELATIVE MONTH` field, which likely represents the number of months relative to the current month (e.g., 0 for the current month, 1 for next month, -1 for last month, etc.).

2. **Filter Conditions**: The filter condition is:
   - `RELATIVE MONTH >= 0 AND RELATIVE MONTH >= 0`

   This essentially means:
   - The `RELATIVE MONTH` must be greater than or equal to 0.

3. **What This Means for Data**:
   - **Included Data**: The filter will include all opportunities that are occurring in the current month (0) and any future months (1, 2, etc.).
   - **Excluded Data**: Any opportunities that occurred in the past months (e.g., -1, -2, etc.) will be excluded from the data set.

In summary, this filter is set up to show only the current and future opportunities, effectively ignoring any past opportunities.)
  - Filter on (Name: `Filterb616ad48471799df27b7`) (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter defined for the data in question. In simple business terms, this means that when this filter is applied, it does not include or exclude any data. Essentially, all data remains visible and accessible because there are no criteria set to limit or refine what data should be shown or hidden.

In practical terms, if you were using this filter in a Power BI report, you would see all the data available in that context without any restrictions. There are no conditions or rules that would change the dataset being analyzed.)
  - Filter on `Opportunity Calendar`.`YEAR MONTH` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Opportunity Calendar`.`YEAR MONTH`. This field likely contains information about the year and month of various opportunities (like sales or projects) in your data.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `YEAR MONTH` field. This means that all available months and years in the dataset will be included in the analysis.

3. **Data Inclusion**: Since the filter is set to include all values, every opportunity from every month and year will be considered. There are no restrictions or exclusions based on the time period.

### Summary:
When this filter is applied, you will see data for every opportunity across all months and years in your reports. There are no limitations, so you get a complete view of your opportunities without any time-based filtering.)

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
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter definition applied in this context. In simple business terms, this means that there are no criteria set to include or exclude any data when this filter is used.

### What This Means:
- **No Data Restrictions**: Since there is no filter defined, all data will be included in any analysis or report where this filter is applied. 
- **Full Visibility**: You will see all records and values without any limitations or exclusions.
- **Default Behavior**: This is essentially the default state, where no filtering is taking place, allowing for a comprehensive view of the dataset.

In summary, when you encounter this filter, you can expect to work with the entire dataset without any data being filtered out.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter defined for the data in question. In simple business terms, this means that when you apply this filter, it does not include or exclude any data. Essentially, it acts as if there is no filter at all.

In practical terms, if you were to use this filter in a Power BI report or dashboard, all the data would be displayed without any restrictions. You would see the complete dataset relevant to your report, as there are no criteria set to limit or refine the data being shown.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter definition applied in this context. In simple business terms, this means that there are no criteria set to include or exclude any data when this filter is applied.

### What This Means:
- **No Data Restrictions**: Since there is no filter defined, all data will be included in any analysis or report. There are no limitations on what data can be viewed or analyzed.
- **Full Visibility**: Users will see all records available in the dataset without any filtering. This is useful when you want to analyze the complete dataset without any specific focus or criteria.

In summary, this filter does not limit or modify the data in any way; it simply allows for a comprehensive view of all available information.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter definition applied in this case. In simple business terms, this means that there are no criteria set to include or exclude any data when this filter is used.

### What This Means:
- **No Data Restrictions**: Since there is no filter defined, all data will be included in any analysis or report where this filter is applied. There are no limitations or exclusions.
- **Full Visibility**: Users will see the complete dataset without any modifications or constraints. This is useful when you want to analyze everything without focusing on specific segments or criteria.

In summary, this filter does not limit or change the data in any way; it simply allows all available data to be viewed and analyzed.)
  - Filter on `Opportunities`.`OpportunitySeq` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Opportunities.OpportunitySeq`. This means that no specific criteria are applied to limit the data shown. 

2. **Data Included**: When this filter is applied, every single opportunity in the dataset will be included in the analysis. There are no exclusions or restrictions based on any conditions.

3. **Practical Implication**: If you are looking at a report or dashboard that uses this filter, you will see all opportunities available in the dataset. This is useful when you want a complete overview without missing any data points.

4. **Use Case**: This type of filter is often used when you want to analyze overall trends, totals, or when you want to ensure that no opportunities are left out of your analysis.

In summary, the filter `(All values)` means that all opportunities are included in the analysis, providing a comprehensive view of the data without any exclusions.)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: In simple business terms, this Power BI filter definition is specifying a condition for the data related to the `Opportunity Calendar` and its `RELATIVE MONTH` field.

Here's what it means:

- The filter is looking at the `RELATIVE MONTH` values, which likely represent months relative to the current date (for example, -1 could mean last month, -2 could mean two months ago, and so on).
- The condition "`RELATIVE MONTH` > -20" means that we are including only those records where the `RELATIVE MONTH` is greater than -20.

In practical terms, this filter will include all opportunities that occurred in the last 19 months (from the current month back to 19 months ago) and exclude any opportunities that are older than that (i.e., those that occurred 20 months ago or earlier).

So, if you apply this filter, you will see data for the last 19 months, ensuring that you are focusing on relatively recent opportunities and not looking at anything that is too far in the past.)

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
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter definition applied in this case. In simple business terms, this means that there are no criteria set to include or exclude any data when this filter is applied.

### Key Points:
- **No Filters Applied**: Since there is no definition, all data will be included in the analysis or report.
- **Full Data Access**: Users will see all available data without any restrictions or limitations.
- **No Specific Criteria**: There are no conditions that would narrow down the data set, such as date ranges, categories, or specific values.

In summary, this filter does not limit or modify the data in any way, allowing for a complete view of the dataset.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter definition applied in this case. In simple business terms, this means that:

- **No Data Restrictions**: There are no criteria set to include or exclude any specific data. Essentially, all data is available for analysis.
- **Full Visibility**: Since there are no filters, you can see all records in the dataset without any limitations. This allows for a comprehensive view of the data.
- **Default State**: This is the default state of a filter, meaning that if you were to apply this filter, it would not change the dataset in any way.

In summary, when this filter is applied, it does not limit or modify the data in any manner, allowing you to work with the entire dataset as it is.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter defined for the data in question. In simple business terms, this means that when this filter is applied, it does not include or exclude any data. Essentially, it acts as if there is no filter at all.

In practical terms, if you were to use this filter in a Power BI report or dashboard, all the data would be displayed without any restrictions. You would see the complete dataset relevant to the report, as there are no criteria set to limit or refine the data being shown.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided indicates that there is no specific filter definition available. In simple business terms, this means that when you apply 'this filter', it does not impose any restrictions or criteria on the data being displayed. 

In practical terms, all data will be included, and nothing will be excluded. Essentially, the filter is neutral, allowing you to see the complete dataset without any limitations or modifications.)
  - Filter on `Opportunities`.`OpportunitySeq` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Opportunities.OpportunitySeq`. This means that no specific criteria are being applied to limit the data. 

2. **Data Included**: When this filter is applied, every single opportunity in the dataset will be considered. There are no exclusions or restrictions, so all opportunities will be visible in your reports.

3. **Use Case**: This type of filter is useful when you want to see the complete picture without any limitations. For example, if you are analyzing sales opportunities and want to review all of them to identify trends or patterns, this filter allows you to do that.

### Summary:
In summary, the filter "(All values)" means that all opportunities are included in the analysis, providing a comprehensive view of the data related to `OpportunitySeq`. There are no opportunities excluded, ensuring that you have access to the full dataset for your analysis.)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: In simple business terms, the provided filter definition JSON is specifying a condition for the `RELATIVE MONTH` field in the `Opportunity Calendar` data. 

Here's what it means:

- **`RELATIVE MONTH`**: This field likely represents a time period in months relative to the current date. For example, it could indicate how many months ago or how many months into the future an opportunity is.

- **`> -20`**: This part of the filter means that we are interested in including all records where the `RELATIVE MONTH` value is greater than -20. 

### What Data is Included:
- The filter will include all opportunities that are from the current month (0) and going back up to 19 months into the past. 
- This means you will see opportunities from the last 19 months, as well as any opportunities from the current month.

### What Data is Excluded:
- Any opportunities that are older than 20 months (i.e., those with a `RELATIVE MONTH` value of -20 or lower) will be excluded from the data set.

### Summary:
In summary, this filter allows you to focus on opportunities that are relevant within the last 20 months, ensuring that you are looking at recent data while excluding anything that is older than that timeframe.)

**lineChart**

- Type: `lineChart`
- Name: `c2d8c28b154bc6a841e2`
- Fields Used:
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Y)
  - `YEAR MONTH` (Query: `Opportunity Calendar.YEAR MONTH`) (Role: Category)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Unknown)
- Visual Level Filters:
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided, `"(No definition found)"`, indicates that there is no specific filter defined. In simple business terms, this means that when you apply 'this filter', it does not impose any restrictions on the data being displayed. 

In practical terms:

- **Included Data**: All data will be included in the report or visualization. There are no criteria to limit or filter out any records.
- **Excluded Data**: No data is excluded because there are no conditions set to remove any records from the view.

In summary, since there is no filter definition, you will see all available data without any limitations.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided indicates that there is no specific filter definition available. In simple business terms, this means that there are no criteria set to include or exclude any data when applying this filter in Power BI.

### What This Means:
- **No Data Restrictions**: Since there is no filter defined, all data will be included in any analysis or visualizations. There are no limits or conditions applied to narrow down the dataset.
- **Full Dataset Access**: Users will see the complete set of data without any filtering, which can be useful for getting an overall view but may not be helpful for focused analysis.

In summary, this filter does not change or limit the data being analyzed; it simply allows all available data to be displayed.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided indicates that there is no specific filter definition available. In simple business terms, this means that when you apply 'this filter', it does not impose any restrictions on the data being displayed. 

In practical terms, all data will be included, and nothing will be excluded. Essentially, the filter is neutral, allowing you to see the complete dataset without any limitations or criteria applied.)
  - Filter on Unknown Target (Type: Advanced, Explanation: The JSON you provided indicates that there is no specific filter definition available. In simple business terms, this means that when you apply 'this filter', it does not impose any restrictions or criteria on the data being displayed. 

In practical terms, all data will be included, and nothing will be excluded. Essentially, the filter is neutral, allowing you to see the complete dataset without any limitations.)
  - Filter on `Opportunities`.`OpportunitySeq` (Type: Advanced, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Opportunities.OpportunitySeq`. This means that no specific criteria are applied to limit the data shown. 

2. **Data Included**: When this filter is applied, every single opportunity in the dataset will be included in the analysis. There are no exclusions based on any conditions or specific values.

3. **Data Excluded**: Since the filter is set to "All values," there are no exclusions. Every opportunity record will be considered, regardless of its characteristics or status.

### Summary:
In simple terms, this filter allows you to see **everything** related to opportunities without any restrictions. You will have a complete view of all opportunities available in the dataset, which is useful when you want to analyze the entire dataset without missing any records.)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: The provided filter definition JSON is used to filter data based on the `RELATIVE MONTH` field in the `Opportunity Calendar`. Let's break it down in simple business terms:

1. **Understanding `RELATIVE MONTH`:** This field likely represents a time frame related to opportunities, where months are counted relative to the current date. For example, `0` could represent the current month, `1` the next month, `-1` the previous month, and so on.

2. **Filter Logic:** The filter condition is:
   - `RELATIVE MONTH >= 0 AND RELATIVE MONTH >= 0`

   However, since both conditions are the same (`RELATIVE MONTH >= 0`), we can simplify this to just one condition:
   - `RELATIVE MONTH >= 0`

3. **What This Means for Data:**
   - The filter includes all records where the `RELATIVE MONTH` is **greater than or equal to 0**. This means:
     - It will include data for the **current month** (where `RELATIVE MONTH` is 0).
     - It will also include data for **future months** (where `RELATIVE MONTH` is 1, 2, etc.).
   - It will **exclude** any records where the `RELATIVE MONTH` is **less than 0** (which would represent past months).

### Summary:
When this filter is applied, you will see only the opportunities that are happening in the current month and any future months, while all past opportunities will be excluded from the view.)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: In simple business terms, this Power BI filter is used to focus on specific outcomes of sales opportunities. The filter is applied to the `Status` field of the `Opportunities` data.

Here's what the filter does:

- **Includes**: It will include only those opportunities that have a status of either **'Lost'** or **'Won'**. This means that if an opportunity has been marked as successfully closed (Won) or unsuccessful (Lost), it will be part of the data being analyzed.

- **Excludes**: Any opportunities that have a status other than 'Lost' or 'Won' will be excluded from the analysis. This could include statuses like 'Open', 'Pending', or any other status that does not indicate a final outcome.

In summary, this filter helps you focus on the final results of sales efforts by only looking at opportunities that have been either won or lost, allowing for a clearer analysis of success rates and outcomes.)
- Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Decision Maker Identified` within the `Opportunities` dataset. This field likely indicates whether a decision maker has been identified for a particular opportunity.

2. **Filter Action**: The filter specifies "(All values)", which means that it does not restrict or limit the data in any way. 

3. **Data Inclusion**: By using this filter, all records from the `Opportunities` dataset will be included in the analysis, regardless of whether a decision maker has been identified or not. 

4. **No Exclusions**: There are no exclusions; every opportunity, whether it has a decision maker identified or not, will be shown in the report.

### Summary:
In simple terms, this filter allows you to see all opportunities without filtering out any based on whether a decision maker has been identified. It ensures that you have a complete view of the data related to opportunities.)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Context**: The filter is applied to the `Opportunities` table, specifically focusing on the `Purchase Process` field.

2. **What It Means**: The filter `(All values)` indicates that **all possible values** for the `Purchase Process` field are included in the data being analyzed. This means that no specific criteria are being applied to limit the data; instead, every opportunity, regardless of its purchase process stage, will be considered.

3. **Inclusion of Data**: Since the filter includes all values, it does not exclude any opportunities based on their purchase process status. For example, whether an opportunity is in the initial stage, negotiation, or closed, all of these will be part of the analysis.

### Summary:
In simple terms, this filter allows you to see **everything** related to the `Purchase Process` in the `Opportunities` data. There are no restrictions, so you get a complete view of all opportunities, regardless of their current status in the purchase process.)
- Filter on `Industries`.`Industry` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** from the `Industries`.`Industry` field. This means that no specific industries are being excluded or included; rather, every industry available in the dataset will be shown.

2. **Data Inclusion**: When this filter is applied, it ensures that all industries—regardless of their type or category—are part of the data being analyzed or displayed. For example, if your dataset includes industries like "Technology," "Healthcare," "Finance," etc., all of these will be visible in your reports.

3. **No Exclusions**: Since the filter specifies "(All values)," there are no restrictions or limitations on the data. This means that if you were to look at a report or visualization, you would see a complete picture of all industries without any filtering out of specific ones.

### Summary:
In simple terms, this filter allows you to see everything related to industries in your data, ensuring that no industry is left out of your analysis.)
- Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are focusing on the data related to the managers of owners in your dataset.

2. **Filter Type**: The filter is set to "(All values)". This indicates that no specific restrictions are being applied to the data. 

3. **Data Inclusion**: By using "(All values)", the filter includes every possible manager in the dataset. This means that all managers, regardless of any specific criteria (like performance, department, etc.), will be shown in the report.

4. **Data Exclusion**: There are no exclusions with this filter. Every manager's data will be visible, and nothing is being left out.

### Summary:
In simple terms, this filter allows you to see data for all managers without any limitations. It ensures that every manager's information is included in the analysis, providing a complete view of the data related to `Owners.Manager`.)
- Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Owners.Owner`. This means that no specific owners are being excluded or included; instead, every owner in the dataset will be considered.

2. **Data Inclusion**: When this filter is applied, it ensures that all owners are visible in your report. For example, if you have a list of owners like "Alice," "Bob," and "Charlie," all of them will be shown in any visualizations or analyses that reference the `Owners.Owner` field.

3. **No Exclusions**: Since the filter is set to "(All values)," there are no restrictions or limitations on the data. This means that you won't miss any owners, and every piece of data related to each owner will be included in your analysis.

### Summary:
In summary, this filter allows you to see the complete picture by including every owner in your data analysis, without filtering out any specific owners. It’s a way to ensure that you have a comprehensive view of all the data related to owners in your reports.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when you apply this filter, you are not excluding any categories of products. 

2. **Data Included**: Every product category available in your dataset will be shown. For example, if your product categories include "Electronics," "Clothing," "Furniture," and "Toys," all of these categories will be included in your report.

3. **Data Excluded**: There are no exclusions with this filter. No product categories are left out, so you will see a complete view of all product categories.

### Summary:
Using this filter means you want to see everything related to product categories without any restrictions. It allows for a comprehensive analysis of all products across all categories in your reports.)
- Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Products.Product`. This means that no specific criteria are being applied to limit the data.

2. **Data Included**: When this filter is applied, every single product in the `Products` dataset will be included in the analysis. There are no exclusions or restrictions, so all products will be visible in your reports.

3. **Data Excluded**: Since the filter is set to "(All values)", there are no products being excluded. Every product, regardless of its attributes (like category, price, availability, etc.), will be part of the data being analyzed.

### Summary:
In simple terms, this filter allows you to see **everything** related to products without any limitations. It’s like saying, “Show me all the products we have, without filtering anything out.”)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the `Purchase Process` field within the `Opportunities` dataset. This field likely contains different stages or types of purchase processes that opportunities go through in your business.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied**. This means that all entries in the `Purchase Process` field will be included in the analysis. 

3. **Data Inclusion**: Since the filter is set to include all values, every opportunity, regardless of its purchase process stage (e.g., "Initial Contact," "Proposal Sent," "Negotiation," etc.), will be considered in any calculations, visualizations, or reports that reference this filter.

4. **Data Exclusion**: There are no exclusions with this filter. All opportunities are visible, and none are filtered out based on the `Purchase Process`.

### Summary:
In summary, applying this filter means you will see all opportunities in your reports, without any restrictions based on their purchase process stages. This is useful when you want a comprehensive view of all opportunities, rather than focusing on a specific subset.)

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
  - Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all possible values** for the `Opportunities`.`Status` field. This means that when this filter is applied, it does not exclude any statuses from the Opportunities data.

2. **Data Included**: Every status that exists in the `Opportunities` dataset will be shown. For example, if the statuses include "Open," "Closed," "Won," and "Lost," all of these statuses will be included in the report or visualization.

3. **Data Excluded**: There are no exclusions with this filter. Since it is set to "(All values)," no opportunities are filtered out based on their status. 

### Summary:
When you apply this filter to the `Opportunities`.`Status`, you are ensuring that all opportunities, regardless of their status, are visible in your analysis. This is useful when you want a complete view of all opportunities without any restrictions based on their current status.)
  - Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: This filter is set to include **all possible values** for the target field, which in this case is `Products.Product`. 

2. **Data Inclusion**: When this filter is applied, it means that every single product in the dataset will be included in the analysis. No products are excluded, so you will see data for all products available.

3. **Use Case**: This is useful when you want to analyze the overall performance of all products without any restrictions. For example, if you are looking at total sales, customer feedback, or inventory levels, this filter ensures that you are considering every product in your calculations and visualizations.

### Summary:
In simple terms, the filter "(All values)" means that you are looking at **everything** related to products—no products are left out. This allows for a comprehensive view of all products in your analysis.)
  - Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when this filter is applied, no specific categories are being excluded or included; instead, every product category available in the dataset will be shown.

2. **Data Inclusion**: Since the filter is set to "(All values)", it ensures that all product categories—such as Electronics, Clothing, Home Goods, etc.—are included in any analysis or visualizations. 

3. **No Exclusions**: There are no restrictions or exclusions applied to the data. This means that if you have products in various categories, all of them will be visible in your reports.

### Summary:
In simple terms, this filter allows you to see everything related to product categories without any limitations. It’s like saying, "Show me all the product categories we have, without leaving anything out.")
  - Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Owner`. This means we are focusing on the data related to the owners of certain items, assets, or entities in your dataset.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied**. This means that all owners will be included in the data being analyzed or displayed.

3. **Data Inclusion**: Since the filter is set to include "All values," every owner in the dataset will be considered. There are no exclusions, so you will see data for every owner without any restrictions.

### Summary:
When this filter is applied to the `Owners.Owner` field, it ensures that all owners are included in your analysis, allowing you to see a complete view of the data without omitting any specific owners.)
  - Filter on `Owners`.`Manager` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Manager`. This means we are looking at the data related to the managers of owners in your dataset.

2. **Filter Type**: The filter is set to "(All values)". This indicates that there are no restrictions on the data being displayed for the `Owners.Manager` field.

3. **Data Inclusion**: By using "(All values)", the filter includes every possible manager in the dataset. This means that all managers, regardless of any specific criteria (like performance, department, or any other attributes), will be shown in the report.

4. **Data Exclusion**: Since the filter is set to include all values, there are no exclusions. No managers are left out of the analysis; every manager's data will be visible.

### Summary:
In summary, this filter allows you to see data for all managers without any limitations. It ensures that every manager's information is included in your analysis, providing a complete view of the data related to `Owners.Manager`.)
  - Filter on `Accounts`.`State or Province` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Accounts`.`State or Province`. This means that when this filter is applied, it does not restrict or limit the data based on any specific states or provinces.

2. **Data Included**: Every single state or province from your dataset will be included in the analysis. For example, if your dataset contains states like California, Texas, and New York, all of these will be shown in your reports.

3. **Data Excluded**: There are no exclusions with this filter. Since it is set to include all values, no states or provinces will be left out of the analysis.

### Summary:
In summary, this filter allows you to see data from every state or province in your `Accounts` dataset without any restrictions. It provides a complete view of all geographic regions represented in your data.)
  - Filter on `Territories`.`Region` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Territories.Region` field. This means that when this filter is applied, no regions are excluded from the data being analyzed or displayed.

2. **Data Inclusion**: Every region in the dataset will be considered. For example, if your dataset includes regions like North, South, East, and West, all of these regions will be shown in your reports.

3. **No Exclusions**: Since the filter specifies "(All values)", there are no restrictions or limitations on the data. This is useful when you want to see a complete overview of all regions without filtering out any specific ones.

### Summary:
When you apply this filter to the `Territories.Region`, you are ensuring that all regions are included in your analysis, allowing for a comprehensive view of the data across all territories.)
  - Filter on `Territories`.`Territory` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the field `Territories.Territory`. This means that no specific territories are being excluded or included; instead, every territory in the dataset will be considered.

2. **Data Inclusion**: When this filter is applied, it ensures that all territories—regardless of their characteristics or attributes—are included in the analysis. For example, if you have territories like "North", "South", "East", and "West", all of these will be shown in your reports.

3. **No Exclusions**: Since the filter specifies "(All values)", there are no territories being filtered out. This is useful when you want to see a complete view of your data without any restrictions.

### Summary:
In summary, this filter allows you to view and analyze data for every territory available in your dataset, providing a comprehensive overview without any limitations.)
  - Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Context**: The filter is applied to the `Opportunities` table, specifically focusing on the `Purchase Process` field.

2. **What It Means**: The filter `(All values)` indicates that **all possible values** for the `Purchase Process` field are included in the analysis. This means that no specific criteria are being applied to limit the data. 

3. **Data Inclusion**: Since the filter includes all values, every opportunity, regardless of its purchase process stage (e.g., initial inquiry, negotiation, closed-won, closed-lost, etc.), will be considered in the report or visualization.

4. **Data Exclusion**: There are no exclusions with this filter. Every opportunity is visible, and none are filtered out based on the `Purchase Process`.

### Summary:
In summary, applying this filter means you are looking at the complete dataset for the `Purchase Process` in the `Opportunities` table without any restrictions. All opportunities will be included in your analysis, allowing for a comprehensive view of the data.)
  - Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and dashboards. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field called `Decision Maker Identified` within the `Opportunities` dataset. This field likely indicates whether a decision maker has been identified for a particular opportunity.

2. **Filter Meaning**: The filter `(All values)` means that **no restrictions** are being applied to the `Decision Maker Identified` field. In other words, all possible values in this field will be included in the data being analyzed.

3. **Data Inclusion**: Since the filter includes all values, it means that whether a decision maker is identified or not, all opportunities will be shown in the report. This could include:
   - Opportunities where a decision maker has been identified.
   - Opportunities where a decision maker has not been identified.

### Summary:
This filter allows you to see every opportunity regardless of whether a decision maker has been identified, providing a complete view of the data without excluding any records.)

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

- Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to control which data is included when analyzing the `RELATIVE MONTH` field in the `Opportunity Calendar`. Let's break it down in simple terms:

1. **`RELATIVE MONTH` > -8**: This part of the filter specifies that we want to include only those records where the `RELATIVE MONTH` value is greater than -8. In practical terms, this means we are looking at months that are within the last 8 months from the current date. For example, if today is October 2023, this filter would include data from January 2023 to October 2023.

2. **NOT (`RELATIVE MONTH` = null)**: This part of the filter ensures that we exclude any records where the `RELATIVE MONTH` value is null (i.e., missing or undefined). This is important because we want to make sure that we are only analyzing complete and valid data.

### Summary:
When this filter is applied to the `Opportunity Calendar`.`RELATIVE MONTH`, it includes all records from the last 8 months (up to the current month) and excludes any records that do not have a defined month value. Essentially, it helps focus the analysis on recent opportunities while ensuring that all included data is valid.)
- Filter on `Opportunities`.`Sales Stage` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the `Sales Stage` field within the `Opportunities` dataset. This field typically represents the different stages that a sales opportunity goes through, such as "Prospecting," "Negotiation," "Closed Won," etc.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied** to the `Sales Stage`. This means that all possible sales stages will be included in the analysis.

3. **Data Inclusion**: Since the filter is set to include "(All values)," every opportunity, regardless of its sales stage, will be considered in the report. This allows for a comprehensive view of all opportunities without excluding any based on their current sales stage.

### Summary:
In summary, this filter allows you to see all opportunities in your report, regardless of their sales stage. It does not exclude any data, ensuring that you have a complete picture of all sales opportunities available in your dataset.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when you apply this filter, you are not excluding any categories of products. Every product category available in your dataset will be shown in your report.

2. **Data Inclusion**: Since the filter is set to "(All values)", it ensures that all product categories—such as Electronics, Clothing, Home Goods, etc.—are included in any analysis or visualizations. No categories are filtered out or hidden.

3. **Use Case**: This type of filter is useful when you want to see a comprehensive view of all product categories without any restrictions. For example, if you are analyzing sales data and want to understand performance across all categories, this filter allows you to see the complete picture.

### Summary:
In summary, the filter definition JSON "(All values)" means that when applied to the `Products`.`Product Category`, it includes every product category in your analysis, ensuring that no data is excluded.)
- Filter on `Owners`.`Owner` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **Target Field**: The filter is applied to the field `Owners.Owner`. This means we are focusing on the data related to the owners of certain items, products, or assets in your dataset.

2. **Filter Meaning**: The phrase "(All values)" indicates that **no specific filtering is being applied**. This means that all owners will be included in the analysis or report. 

3. **Data Inclusion**: Since the filter is set to include all values, every owner in the dataset will be visible. There are no restrictions or exclusions based on owner names or any other criteria.

### Summary:
When this filter is applied, you will see data for **every owner** in your reports, allowing you to analyze the performance or characteristics of all owners without any limitations.)
- Filter on `Products`.`Product` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Simple Business Terms:

1. **What It Means**: The filter is set to include **all values** for the target field, which in this case is `Products.Product`. This means that no specific criteria are being applied to limit the data.

2. **Data Included**: When this filter is applied, every single product in the dataset will be included in the report or visualization. There are no exclusions or restrictions.

3. **Business Impact**: This is useful when you want to see a complete overview of all products without filtering out any specific ones. For example, if you are analyzing sales data, applying this filter allows you to see sales figures for every product available, giving you a comprehensive view of your product performance.

### Summary:
In summary, the filter `(All values)` means that all products will be shown in your report, allowing for a full analysis without any data being left out.)
- Filter on `Products`.`Product Category` (Type: Categorical, Explanation: In Power BI, filters are used to control which data is displayed in your reports and visualizations. The filter definition JSON you provided is:

```json
"(All values)"
```

### Explanation in Business Terms:

1. **What It Means**: The filter is set to include **all values** for the `Product Category` field. This means that when you apply this filter, you are not excluding any categories of products. Every product category available in your dataset will be shown in your report.

2. **Data Inclusion**: Since the filter is set to "(All values)", it ensures that all product categories—such as Electronics, Clothing, Home Goods, etc.—are included in the analysis. No categories are filtered out, so you will see a complete view of all products.

3. **No Exclusions**: There are no restrictions or exclusions applied to the data. This is useful when you want to analyze or visualize the performance of all product categories without limiting the scope to specific ones.

### Summary:
In summary, this filter allows you to see **everything** related to `Product Category` in your Power BI report, ensuring that no product categories are left out of your analysis.)

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
  - Filter on `Owners`.`[Rev Goal]` (Type: Advanced, Explanation: In simple business terms, the provided Power BI filter definition JSON:

```json
"`?` <> 0M"
```

is specifying a condition that filters the data based on the `Owners`.`[Rev Goal]` field. Here's what it means:

- The symbol `?` represents the `Owners`.`[Rev Goal]` value for each record in your dataset.
- The condition `<> 0M` means "not equal to zero." The `M` indicates that the value is a monetary amount.

So, when this filter is applied, it will **include only those records where the revenue goal (`[Rev Goal]`) is greater than or less than zero**. In other words, it **excludes any records where the revenue goal is exactly zero**.

### Summary:
- **Included**: Records with a revenue goal that is either positive or negative (i.e., any value except zero).
- **Excluded**: Records where the revenue goal is exactly zero. 

This filter helps focus on owners who have a defined revenue goal, whether it's a target to achieve (positive) or a deficit (negative), while ignoring those who have no goal set at all (zero).)

**Closing Percentages**

- Type: `barChart`
- Name: `d6c5d8ceebb55162083f`
- Fields Used:
  - `Product Category` (Query: `Products.Product LOB`) (Role: Category)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Tooltips)
  - `Product` (Query: `Products.Product`) (Role: Category)
  - `Close %` (Query: `Opportunities.Close %`) (Role: Y)
- Visual Level Filters:
  - Filter on `Owners`.`[Rev Goal]` (Type: Advanced, Explanation: In simple business terms, the provided Power BI filter definition JSON is specifying a condition that filters the data based on the `Rev Goal` field in the `Owners` table.

Here's what the filter means:

- **`?`**: This represents the value in the `Rev Goal` field for each record in the `Owners` table.
- **`<>`**: This is a comparison operator that means "not equal to."
- **`0M`**: This indicates the value zero in millions (0 million).

Putting it all together, the filter "`?` <> 0M" means:

**Include only those records where the `Rev Goal` is not equal to zero million.**

In practical terms, when this filter is applied, any records in the `Owners` table that have a `Rev Goal` of zero million will be excluded from the analysis. Only records with a `Rev Goal` greater than or less than zero million will be included. This helps focus on owners who have a revenue goal that is meaningful and not just a placeholder of zero.)

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
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: In simple business terms, the provided filter definition JSON is specifying a condition for the `RELATIVE MONTH` field in the `Opportunity Calendar` data. 

Here's what it means:

- **`RELATIVE MONTH`**: This field likely represents a time frame related to opportunities, where months are counted relative to the current date. For example, `0` might represent the current month, `1` the next month, `-1` the previous month, and so on.

- **`>= 0`**: The filter is saying to include only those records where the `RELATIVE MONTH` is greater than or equal to zero. 

### What Data is Included or Excluded:
- **Included**: This filter will include all opportunities that are occurring in the current month (where `RELATIVE MONTH` is `0`) and in any future months (where `RELATIVE MONTH` is `1`, `2`, etc.).

- **Excluded**: It will exclude any opportunities that occurred in the past (where `RELATIVE MONTH` is `-1`, `-2`, etc.).

### Summary:
In summary, this filter is used to focus on current and future opportunities, ignoring any that have already happened in the past. This is useful for businesses looking to analyze or report on upcoming sales opportunities.)

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

