# Power BI Model & Report Documentation

*Generated on: 2025-06-06 12:15:55*

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

The Power BI data model appears to represent a comprehensive Customer Relationship Management (CRM) system, likely focused on sales and marketing activities within a business. The inclusion of tables such as 'Accounts', 'Contacts', 'Opportunities', and 'Campaigns' suggests a strong emphasis on managing customer relationships, tracking sales opportunities, and analyzing marketing efforts. The relationships between these tables indicate a structured approach to linking customers (Accounts and Contacts) with their respective sales opportunities and marketing campaigns, facilitating insights into customer engagement and sales performance.

Additionally, the presence of tables like 'Industries', 'Products', 'Territories', and 'Opportunity Calendar' highlights the model's capability to analyze sales data across different sectors, product lines, and geographical regions. The 'Opportunity Forecast Adjustment' table suggests a focus on refining sales forecasts based on various factors, enhancing the decision-making process. Overall, this data model is likely designed to provide a holistic view of the sales pipeline, customer interactions, and marketing effectiveness, enabling businesses to optimize their strategies and drive revenue growth.

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

### <a name="tables"></a>Tables

#### <a name="table-accounts"></a>Table: `Accounts`

The 'Accounts' table serves as a comprehensive repository of customer account information, detailing key attributes such as account identifiers, geographic locations, and ownership, which enables businesses to analyze customer demographics, manage relationships, and optimize sales strategies across various territories and industries.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Account Name` | `string` | The 'Account Name' column stores the names of customer accounts, serving as a key identifier for managing and referencing account-related data within the Accounts table. |
| `Account Number` | `string` | The 'Account Number' column stores unique identifiers for each account, facilitating accurate tracking and management of customer accounts within the Accounts table. |
| `AccountID` | `string` | The 'AccountID' column uniquely identifies each account in the Accounts table, facilitating efficient data retrieval and management. |
| `AccountOwnerSeq` | `int64` | The 'AccountOwnerSeq' column (int64) uniquely identifies the sequence number of the account owner associated with each account in the Accounts table. |
| `AccountSeq` | `int64` | Column Description: The 'AccountSeq' column serves as a unique sequential identifier for each account in the Accounts table, facilitating efficient data retrieval and management. |
| `Country` | `string` | The 'Country' column stores the name of the country associated with each account, facilitating geographic analysis and segmentation of account data. |
| `IndustrySeq` | `int64` | Column Description: The 'IndustrySeq' column (int64) uniquely identifies the sequence number of the industry associated with each account, facilitating efficient categorization and analysis of accounts by industry type. |
| `State or Province` | `string` | Column Description: This column captures the state or province associated with each account, facilitating regional analysis and targeted marketing strategies. |
| `TerritorySeq` | `int64` | Column Description: The 'TerritorySeq' column (int64) uniquely identifies the sequence number of the territory associated with each account, facilitating efficient territory management and reporting. |

---

#### <a name="table-campaigns"></a>Table: `Campaigns`

The 'Campaigns' table serves as a central repository for tracking and managing marketing initiatives, detailing each campaign's unique identifier, type, and name. This enables businesses to analyze campaign performance, optimize marketing strategies, and enhance overall engagement with target audiences.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Campaign` | `string` | The 'Campaign' column stores the names or identifiers of marketing campaigns, enabling the tracking and analysis of their performance and impact within the overall marketing strategy. |
| `Campaign Type` | `string` | Column Description: This column categorizes the type of marketing campaign, such as email, social media, or paid advertising, to facilitate targeted analysis and reporting within the Campaigns table. |
| `CampaignSeq` | `int64` | The 'CampaignSeq' column represents a unique sequential identifier for each marketing campaign, facilitating the tracking and management of campaign data within the 'Campaigns' table. |

---

#### <a name="table-contacts"></a>Table: `Contacts`

The 'Contacts' table serves as a centralized repository for managing key stakeholder information, including their job titles and associated accounts, facilitating effective communication and relationship management within the organization. This table enables businesses to track and analyze interactions with contacts, enhancing customer engagement and support strategies.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `AccountSeq` | `int64` | The 'AccountSeq' column (int64) in the 'Contacts' table uniquely identifies the sequence number of each account associated with a contact, facilitating efficient data retrieval and management. |
| `Contact` | `string` | The 'Contact' column stores the names and details of individuals or organizations for the purpose of enriching data through interactions with a large language model. |
| `ContactSeq` | `int64` | Column Description: A unique sequential identifier for each contact record in the Contacts table, facilitating efficient data retrieval and management. |
| `Job Title` | `string` | The 'Job Title' column captures the professional designation of each contact, providing essential context for understanding their role and responsibilities within their organization. |

---

#### <a name="table-industries"></a>Table: `Industries`

The 'Industries' table serves as a reference dataset that categorizes various sectors of the economy, enabling businesses to analyze performance metrics and trends by industry type. The inclusion of an industry sequence number facilitates efficient sorting and organization of industry data for reporting and analytical purposes.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Industry` | `string` | The 'Industry' column categorizes various sectors of the economy, providing essential context for data enrichment and analysis within the Industries table. |
| `IndustrySeq` | `int64` | The 'IndustrySeq' column (int64) serves as a unique sequential identifier for each industry entry in the 'Industries' table, facilitating efficient data retrieval and organization. |

---

#### <a name="table-opportunities"></a>Table: `Opportunities`

The 'Opportunities' table captures critical information about potential sales deals, including their current status, value, and likelihood of closing, enabling sales teams to prioritize efforts and forecast revenue effectively. By tracking key metrics such as decision maker identification, sales stage, and discount levels, this table supports strategic decision-making and enhances overall sales performance.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `AccountSeq` | `int64` | Column Description: The 'AccountSeq' column (int64) uniquely identifies the sequence number of the associated account for each opportunity, facilitating efficient data retrieval and relationship mapping within the Opportunities table. |
| `CampaignSeq` | `int64` | The 'CampaignSeq' column (int64) in the 'Opportunities' table uniquely identifies the sequence number of marketing campaigns associated with each opportunity, facilitating the tracking and analysis of campaign effectiveness. |
| `CloseDate` | `dateTime` | The 'CloseDate' column represents the date and time when an opportunity is expected to be finalized, serving as a critical timestamp for sales forecasting and performance tracking within the Opportunities table. |
| `DateDiff-Days` | `int64` | Column Description: The 'DateDiff-Days' column represents the number of days between key dates in the opportunity lifecycle, providing insights into the duration of each opportunity's progression. |
| `DaysToClose` | `int64` | The 'DaysToClose' column represents the number of days required to finalize a sales opportunity, providing insights into the sales cycle duration for better forecasting and resource allocation. |
| `Decision Maker Identified` | `boolean` | Indicates whether a decision maker has been identified for the opportunity, facilitating targeted engagement strategies. |
| `Discount` | `double` | The 'Discount' column (double) in the 'Opportunities' table represents the monetary reduction applied to the total value of an opportunity, facilitating the assessment of pricing strategies and revenue projections. |
| `Opportunity Created On` | `dateTime` | The 'Opportunity Created On' column records the date and time when each sales opportunity was initiated, providing a timestamp for tracking the lifecycle of opportunities within the business. |
| `OpportunitySeq` | `int64` | The 'OpportunitySeq' column (int64) uniquely identifies each opportunity record in the Opportunities table, facilitating efficient tracking and management of sales prospects. |
| `Probability` | `double` | The 'Probability' column represents the likelihood, expressed as a decimal value, of successfully closing a sales opportunity, aiding in prioritization and forecasting efforts. |
| `Probability (raw)` | `double` | The 'Probability (raw)' column represents the unadjusted likelihood, expressed as a double value, that an opportunity will convert into a successful outcome, aiding in data-driven decision-making for sales strategies. |
| `ProductSeq` | `int64` | Column Description: The 'ProductSeq' column (int64) uniquely identifies the sequence of products associated with each opportunity, facilitating the tracking and management of product offerings within the sales pipeline. |
| `Purchase Process` | `string` | The 'Purchase Process' column captures the current stage or steps involved in the buyer's journey for each opportunity, providing insights into the progression and status of potential sales. |
| `Rating` | `string` | The 'Rating' column captures qualitative assessments of each opportunity, allowing stakeholders to gauge potential value and prioritize actions based on subjective evaluations. |
| `Sales Stage` | `string` | The 'Sales Stage' column categorizes the current phase of each opportunity in the sales process, providing insights into the progression and potential value of deals within the Opportunities table. |
| `Status` | `string` | The 'Status' column indicates the current stage or condition of each opportunity, providing essential insights for tracking progress and decision-making in the sales pipeline. |
| `SystemUserSeq` | `int64` | Column Description: The 'SystemUserSeq' column (int64) uniquely identifies the system user associated with each opportunity, facilitating user-specific tracking and management of sales activities. |
| `Value` | `int64` | The 'Value' column represents the monetary worth of each opportunity, quantified as an integer, to facilitate financial analysis and decision-making within the Opportunities table. |

##### Calculated Columns

**`Blank`** (`string`)

- **Description:** The 'Blank' column is intended to hold placeholder or unused string values within the Opportunities table, serving as a potential marker for future data enrichment or categorization.
- **DAX Expression:**
```dax
BLANK()
```
- **DAX Explanation (Generated):** The DAX expression `BLANK()` is used to create a calculated column that contains no value, essentially representing an empty or null state. 

In simple business terms, when you use `BLANK()` in a calculated column, you are telling the system that for every row in that column, there should be no data recorded. This can be useful in various scenarios, such as:

1. **Placeholder for Future Data**: If you plan to populate this column with data later but want to keep the structure of your data model intact for now, using `BLANK()` allows you to indicate that the data is currently unavailable.

2. **Conditional Logic**: You might want to use `BLANK()` in conjunction with other calculations or conditions. For example, if certain criteria are not met, you can return `BLANK()` instead of a value, which can help in filtering or visualizing data more effectively.

3. **Data Cleansing**: If you are cleaning up your data and want to mark certain rows as having no applicable value, `BLANK()` can serve that purpose.

Overall, using `BLANK()` helps maintain clarity in your data model by explicitly indicating where values are missing or not applicable.

**`Days Remaining In Pipeline`** (`string`)

- **Description:** Column Description: This column indicates the number of days left for each opportunity to progress through the sales pipeline, represented as a string for easy readability.
- **DAX Expression:**
```dax
IF(Opportunities[Status]="Open", DATEDIFF(TODAY(),Opportunities[CloseDate],DAY),0)
```
- **DAX Explanation (Generated):** This DAX code snippet is used to create a calculated column called 'Days Remaining In Pipeline' for a dataset of opportunities. Here's a breakdown of what it does in simple business terms:

1. **Condition Check**: The expression starts with an `IF` statement that checks if the status of an opportunity is "Open". This means it only considers opportunities that are currently active and not yet closed.

2. **Calculate Days Remaining**: If the opportunity is "Open", it calculates the number of days remaining until the opportunity's close date. This is done using the `DATEDIFF` function, which takes three arguments:
   - `TODAY()`: This function gets the current date.
   - `Opportunities[CloseDate]`: This is the date when the opportunity is expected to close.
   - `DAY`: This specifies that the difference should be calculated in days.

   So, if the opportunity is still open, the formula calculates how many days are left from today until the close date.

3. **Return Value**: If the opportunity is not "Open" (meaning it could be "Closed" or in another status), the formula returns 0. This indicates that there are no days remaining in the pipeline for opportunities that are not currently active.

### Summary:
In summary, this DAX expression calculates the number of days remaining for open opportunities until their expected close date. If an opportunity is not open, it simply returns 0. This helps businesses track how much time is left to close active deals in their sales pipeline.

**`Days Remaining In Pipeline (bins)`** (`string`)

- **Description:** Column Description: This column categorizes the remaining days in the sales pipeline into predefined bins, facilitating quick assessment of opportunity urgency and prioritization for sales teams.

**`Weeks Open`** (`string`)

- **Description:** Column Description: This column indicates the duration, in weeks, that each opportunity has been active or open for engagement, represented as a string.

##### Measures

**`Close %`**

- **DAX Expression:**
```dax
[Count of Won]/([Count of Won]+[Count of Lost])
```
- **DAX Explanation (Generated):** The DAX expression you provided calculates the "Close %" measure, which represents the percentage of successful sales or deals that were won compared to the total number of deals (both won and lost).

Here's a breakdown of the components:

1. **[Count of Won]**: This part counts the number of deals that were successfully closed or won.

2. **[Count of Lost]**: This part counts the number of deals that were not successful or lost.

3. **([Count of Won] + [Count of Lost])**: This adds together the number of won and lost deals to get the total number of deals that were considered.

4. **[Count of Won] / ([Count of Won] + [Count of Lost])**: Finally, this divides the number of won deals by the total number of deals (won + lost). 

### What It Achieves:
- The result of this calculation is a decimal value that represents the proportion of deals that were won out of all deals. 
- To express it as a percentage, you would typically multiply the result by 100.
- For example, if there were 70 won deals and 30 lost deals, the calculation would be 70 / (70 + 30) = 70 / 100 = 0.70, or 70%. This means that 70% of the deals were successful.

In summary, this measure helps businesses understand their success rate in closing deals, which is crucial for evaluating sales performance and making informed decisions about sales strategies.

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
- **DAX Explanation (Generated):** This DAX code snippet is designed to calculate the number of opportunities that have a status of "Lost" within a dataset called `Opportunities`. Here’s a breakdown of what each part of the code does in simple business terms:

1. **COUNTAX**: This function counts the number of rows that meet certain criteria. In this case, it will count the opportunities that are filtered based on their status.

2. **FILTER**: This function is used to create a subset of the `Opportunities` table. It filters the data to include only those opportunities where the `Status` column equals "Lost". Essentially, it narrows down the dataset to just the opportunities that are marked as lost.

3. **KEEPIFILTERS**: This function ensures that any existing filters applied to the `Opportunities` table remain in effect while adding the new filter for "Lost" status. This means that if there are other filters (like date ranges or sales regions) already applied, they will still be considered in the calculation.

4. **Opportunities[OpportunitySeq]**: This refers to a specific column in the `Opportunities` table, which likely contains unique identifiers for each opportunity. The `COUNTAX` function will count the number of these unique identifiers in the filtered set.

### What It Achieves:
In summary, this DAX measure calculates the total number of opportunities that have been marked as "Lost," while respecting any other filters that may be applied to the data. This is useful for businesses to understand how many potential sales were not successful, helping them analyze performance and identify areas for improvement.

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
- **DAX Explanation (Generated):** This DAX code snippet is designed to create a measure called 'Count of Won' that counts the number of opportunities in a business context that have been marked as "Won." Here’s a breakdown of what each part of the code does in simple terms:

1. **FILTER Function**: The `FILTER` function is used to narrow down the data in the 'Opportunities' table. It looks at each row in the 'Opportunities' table and checks if the 'Status' of that opportunity is "Won." This means that only the opportunities that have been successfully closed (won) will be considered in the next steps.

2. **KEEPFILTERS Function**: The `KEEPFILTERS` function ensures that any existing filters applied to the 'Opportunities' table (like filters from a report or dashboard) are preserved while adding the new filter for "Won" status. This allows the measure to be dynamic and responsive to other filters that might be applied in the report.

3. **COUNTAX Function**: The `COUNTAX` function counts the number of rows that meet the criteria defined in the `FILTER` function. Specifically, it counts the 'OpportunitySeq' column for the filtered opportunities. Essentially, it counts how many opportunities have been marked as "Won."

### Summary:
In summary, this DAX measure calculates the total number of opportunities that have been successfully won, taking into account any other filters that might be applied in the report. This helps businesses understand their success rate in closing deals and can be used for performance analysis and reporting.

**`Forecast`**

- **DAX Expression:**
```dax
([Revenue Won]+[Revenue In Pipeline])
```
- **DAX Explanation (Generated):** This DAX expression calculates the total expected revenue by adding two key components together:

1. **Revenue Won**: This represents the actual revenue that has already been secured or confirmed from sales. It reflects the income that the business has successfully generated from completed transactions.

2. **Revenue In Pipeline**: This refers to the potential revenue that is anticipated from sales opportunities that are currently being pursued but have not yet been finalized. This could include deals that are in negotiation or awaiting approval.

By adding these two figures together, the measure provides a forecast of total revenue, combining both confirmed income and potential future income. This helps businesses understand their overall financial outlook and make informed decisions based on both current and anticipated sales performance.

**`Forecast %`**

- **DAX Expression:**
```dax
(([Revenue Won]+[Revenue In Pipeline]))/ [Rev Goal]
```
- **DAX Explanation (Generated):** This DAX code snippet calculates the percentage of revenue that has been achieved or is expected to be achieved compared to a predefined revenue goal. Here’s a breakdown of what each part does:

1. **Revenue Won**: This represents the actual revenue that has been successfully earned or closed. It reflects the sales that have been finalized.

2. **Revenue In Pipeline**: This indicates the revenue that is expected to be earned from potential sales that are currently in progress but have not yet been finalized. It includes deals that are likely to close in the future.

3. **Rev Goal**: This is the target revenue that the business aims to achieve within a specific period.

4. **Calculation**: The expression adds together the revenue that has already been won and the revenue that is still in the pipeline. This total is then divided by the revenue goal.

5. **Result**: The final result is a percentage that shows how much of the revenue goal has been met or is expected to be met based on current sales performance and potential future sales.

In simple terms, this measure helps the business understand its progress towards its revenue targets by combining what has been earned and what is anticipated, allowing for better planning and decision-making.

**`Forecast by Win/Loss Ratio`**

- **DAX Expression:**
```dax
[Revenue Open] * [Close %]
```
- **DAX Explanation (Generated):** The DAX expression you provided is used to calculate a measure called "Forecast by Win/Loss Ratio." Let's break it down in simple business terms:

1. **[Revenue Open]**: This part of the expression represents the total revenue that is currently open or in the pipeline. It includes all potential sales that have not yet been finalized. Think of it as the total amount of money that the business expects to earn from deals that are still being negotiated or are in progress.

2. **[Close %]**: This part represents the percentage likelihood that these open deals will actually close successfully. It reflects the company's confidence in converting these potential sales into actual revenue. For example, if the Close % is 70%, it means the business believes there is a 70% chance that the open deals will result in sales.

3. **Multiplication**: By multiplying [Revenue Open] by [Close %], the expression calculates the expected revenue from the open deals. Essentially, it estimates how much revenue the business can realistically expect to earn based on the current open opportunities and their likelihood of closing.

### What It Achieves:
The overall goal of this DAX expression is to provide a forecast of potential revenue based on the current sales pipeline. It helps the business understand not just how much revenue is available, but how much of that revenue is likely to be realized based on the probability of closing those deals. This forecast can be crucial for planning, budgeting, and making informed business decisions.

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
			        )
			    )
```
- **DAX Explanation (Generated):** The DAX code snippet you provided is used to create a measure called "Opportunity Count In Pipeline." Here's a breakdown of what it does in simple business terms:

1. **Purpose**: This measure counts the number of opportunities that are currently in the pipeline, specifically those that are "Open."

2. **Components**:
   - **CALCULATE**: This function changes the context in which data is evaluated. In this case, it is used to modify the counting of opportunities based on certain criteria.
   - **COUNT(Opportunities[Value])**: This part counts the number of entries in the "Value" column of the "Opportunities" table. Essentially, it counts how many opportunities there are.
   - **FILTER(Opportunities, Opportunities[Status] = "Open")**: This function filters the "Opportunities" table to include only those rows where the "Status" is "Open." This means that only opportunities that are currently active and not closed or lost will be considered in the count.

3. **What it Achieves**: The overall result of this measure is a count of all the opportunities that are still active in the sales pipeline. It helps businesses understand how many potential deals are currently being pursued, which is crucial for sales forecasting and resource allocation.

In summary, this DAX measure provides a clear view of the number of active sales opportunities, helping businesses track their sales pipeline effectively.

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
- **DAX Explanation (Generated):** This DAX code snippet calculates a measure called "Revenue In Pipeline," which represents the expected revenue from sales opportunities that are currently open and at a certain stage in the sales process. Here’s a breakdown of what it does in simple business terms:

1. **Identify Open Opportunities**: The code first looks at a table called `Opportunities`, which contains various sales opportunities. It filters this table to only include opportunities that are currently "Open" and have a sales stage that is considered advanced (specifically, where the first character of the `Sales Stage` is 2 or higher).

2. **Calculate Total Value**: For the filtered opportunities, it sums up their values (the potential revenue from each opportunity). This total is stored in a variable called `Revenue`.

3. **Adjust for Forecasting**: After calculating the total revenue from the open opportunities, the code then adjusts this amount based on a forecast adjustment value. This adjustment is expressed as a percentage (from the `Opportunity Forecast Adjustment` table). The adjustment is calculated by taking the total revenue and adding a percentage of it based on the forecast adjustment value.

4. **Final Output**: The final result is the total expected revenue from the open opportunities, including any adjustments based on forecast changes. This gives a more accurate picture of the revenue that the business can expect to realize from its current sales pipeline.

In summary, this DAX measure helps businesses understand how much revenue they can anticipate from their current sales opportunities, factoring in both the status of those opportunities and any adjustments based on forecasting.

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
- **DAX Explanation (Generated):** This DAX code snippet is designed to calculate the total revenue from opportunities that have been marked as "Won." Here's a breakdown of what each part does in simple business terms:

1. **CALCULATE**: This function changes the context in which data is evaluated. In this case, it is used to modify the calculation to focus only on certain opportunities.

2. **SUMX(Opportunities, Opportunities[Value])**: This part of the code sums up the values of the opportunities. The `SUMX` function iterates over each opportunity in the `Opportunities` table and adds up the `Value` associated with each one. Essentially, it calculates the total revenue from all opportunities.

3. **FILTER(Opportunities, Opportunities[Status] = "Won")**: This function filters the `Opportunities` table to include only those opportunities where the `Status` is "Won." It narrows down the data set to just the successful opportunities.

Putting it all together, this DAX expression calculates the total revenue from all opportunities that have been successfully won. It ensures that only the relevant opportunities (those marked as "Won") are included in the revenue calculation. The end result is a measure that provides insight into how much revenue has been generated from successful sales opportunities.

**`Revenue Won Average Deal Size`**

- **DAX Expression:**
```dax
AVERAGEX(Opportunities,[Revenue Won])
```
- **DAX Explanation (Generated):** The DAX expression you provided calculates the average deal size of revenue won from opportunities. Let's break it down:

1. **AVERAGEX**: This is a DAX function that calculates the average of a set of values. It takes two arguments: a table (or a set of rows) and an expression that defines the values to average.

2. **Opportunities**: This refers to a table or dataset that contains information about various sales opportunities. Each row in this table represents a different opportunity that a business is pursuing.

3. **[Revenue Won]**: This is a measure or column that represents the revenue that has been successfully won from each opportunity. It indicates how much money was generated from closed deals.

### What It Achieves:
The expression `AVERAGEX(Opportunities,[Revenue Won])` calculates the average revenue won across all opportunities in the dataset. In simpler terms, it tells you how much revenue, on average, is generated from each successful deal. 

This measure is useful for understanding the typical size of deals that are being closed, which can help in sales forecasting, performance analysis, and strategic planning. By knowing the average deal size, a business can better assess its sales performance and set realistic revenue targets.

---

#### <a name="table-opportunity-calendar"></a>Table: `Opportunity Calendar`

The 'Opportunity Calendar' table serves as a comprehensive time-based reference for tracking and analyzing business opportunities, enabling users to filter and segment data by various time dimensions such as day, week, month, and year. This structured calendar format supports effective reporting and forecasting by aligning opportunity data with specific time periods, facilitating strategic decision-making and performance evaluation.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Date` | `string` | Column Description: The 'Date' column stores the scheduled date for each opportunity, formatted as a string, to facilitate tracking and management of events within the Opportunity Calendar. |
| `DAY` | `string` | Column Description: The 'DAY' column represents the specific day of the week associated with each opportunity, facilitating time-based analysis and scheduling within the Opportunity Calendar. |
| `DaySeq` | `string` | The 'DaySeq' column represents a sequential identifier for each day in the Opportunity Calendar, facilitating the organization and retrieval of daily opportunities in a structured format. |
| `MONTH` | `string` | The 'MONTH' column (string) in the 'Opportunity Calendar' table represents the name of the month associated with each opportunity, facilitating time-based analysis and reporting. |
| `MONTH NUMBER` | `string` | The 'MONTH NUMBER' column (string) in the 'Opportunity Calendar' table represents the numerical designation of each month, facilitating the organization and analysis of opportunities by their respective timeframes. |
| `RELATIVE 07 DAY PERIOD` | `string` | The 'RELATIVE 07 DAY PERIOD' column captures a string representation of a specific seven-day timeframe relative to the opportunity's timeline, facilitating temporal analysis and decision-making within the Opportunity Calendar. |
| `RELATIVE 30 DAY PERIOD` | `string` | The 'RELATIVE 30 DAY PERIOD' column indicates the timeframe of the last 30 days relative to the current date, providing context for opportunity tracking and analysis within the Opportunity Calendar. |
| `RELATIVE DAY` | `string` | The 'RELATIVE DAY' column indicates the specific day in relation to a defined reference point within the Opportunity Calendar, facilitating the tracking and analysis of opportunities over time. |
| `RELATIVE MONTH` | `string` | The 'RELATIVE MONTH' column in the Opportunity Calendar table represents the month in relation to the current date, facilitating time-based analysis of opportunities. |
| `RELATIVE WEEK` | `string` | The 'RELATIVE WEEK' column indicates the week number relative to a specified reference date, facilitating the tracking and analysis of opportunities over time within the Opportunity Calendar. |
| `WEEK` | `string` | The 'WEEK' column represents the specific week identifier for each opportunity, formatted as a string, to facilitate time-based analysis and reporting within the Opportunity Calendar. |
| `YEAR` | `string` | The 'YEAR' column (string) in the Opportunity Calendar table captures the specific year associated with each opportunity, facilitating time-based analysis and reporting. |
| `YEAR MONTH` | `string` | The 'YEAR MONTH' column (string) in the Opportunity Calendar table represents the specific year and month associated with each opportunity, facilitating time-based analysis and reporting. |
| `YEAR MONTH NUMBER` | `string` | The 'YEAR MONTH NUMBER' column stores a string representation of the year and month, facilitating the organization and analysis of opportunities within the Opportunity Calendar. |
| `YEAR WEEK` | `string` | The 'YEAR WEEK' column represents the specific year and week number of each opportunity, formatted as a string, to facilitate time-based analysis and reporting within the Opportunity Calendar. |

---

#### <a name="table-opportunity-forecast-adjustment"></a>Table: `Opportunity Forecast Adjustment`

The 'Opportunity Forecast Adjustment' table is designed to capture and manage modifications to sales forecasts, enabling businesses to refine their revenue projections based on updated insights or strategic decisions. This table facilitates better decision-making by providing a clear record of adjustments made to forecasts, ensuring alignment with current market conditions and organizational goals.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Forecast Adjustment` | `string` | The 'Forecast Adjustment' column captures qualitative modifications to the projected sales figures, allowing for nuanced insights into expected performance variations within the Opportunity Forecast Adjustment table. |

##### Calculated Columns

**`Blank`** (`string`)

- **Description:** The 'Blank' column is intended to hold placeholder values or notes that may not currently contain data but are reserved for future use in the Opportunity Forecast Adjustment table.
- **DAX Expression:**
```dax
1
```
- **DAX Explanation (Generated):** It seems like you've provided a very simple DAX expression that consists of just the number `1`. In the context of a calculated column in a data model, this expression will create a new column where every row in that column will have the value `1`.

### What it Achieves:
- **Uniform Value**: Every entry in this new calculated column will be `1`. This means that regardless of the data in other columns, this column will always show `1` for each row.
- **Potential Use Cases**: 
  - **Counting**: This column can be useful for counting purposes. For example, if you want to count the number of rows in a table, you can sum this column, and it will give you the total number of rows.
  - **Grouping**: It can also be used to create groups in visualizations or calculations where you want to treat all rows equally.

In summary, this DAX expression creates a calculated column that assigns the value `1` to every row, which can be useful for counting or grouping data in analyses.

##### Measures

**`Fcst adj slicer alt text`**

- **DAX Expression:**
```dax
CONCATENATE("Use the slicer to adjust the forecast, current value is ", 'Opportunity Forecast Adjustment'[Forecast Adjustment Value])
```
- **DAX Explanation (Generated):** This DAX code snippet creates a text message that provides guidance to users about how to interact with a forecast adjustment feature in a report or dashboard.

Here's a breakdown of what it does:

1. **CONCATENATE Function**: The `CONCATENATE` function is used to combine two pieces of text into one single string.

2. **Static Text**: The first part of the text is a fixed message: "Use the slicer to adjust the forecast, current value is ". This part informs the user that they can use a slicer (a filtering tool) to modify the forecast.

3. **Dynamic Value**: The second part of the text pulls in a dynamic value from the data model: `'Opportunity Forecast Adjustment'[Forecast Adjustment Value]`. This value represents the current forecast adjustment that has been made by the user or is being displayed.

4. **Final Output**: When combined, the final output of this DAX expression will be a complete sentence that tells the user what they can do (adjust the forecast using the slicer) and shows them the current value of the forecast adjustment.

### In Simple Business Terms:
This DAX measure generates a helpful message for users, letting them know they can change the forecast using a slicer and showing them the current adjustment value. It enhances user experience by providing clear instructions and relevant information in one concise statement.

**`Forecast Adjustment Value`**

- **DAX Expression:**
```dax
SELECTEDVALUE('Opportunity Forecast Adjustment'[Forecast Adjustment], 0)
```
- **DAX Explanation (Generated):** The DAX expression you provided is used to retrieve a specific value from a column in a data table, and it has a fallback option if no value is selected. Here’s a breakdown of what it does in simple business terms:

1. **Context of Use**: This expression is likely used in a report or dashboard where users can select different options related to "Forecast Adjustments" for opportunities in a business context, such as sales forecasts.

2. **SELECTEDVALUE Function**: The function `SELECTEDVALUE` is designed to return the value of a column when there is a single value selected. In this case, it looks at the column `'Opportunity Forecast Adjustment'[Forecast Adjustment]`.

3. **Fallback Value**: The second part of the function, `0`, is a default value that will be returned if there is no single value selected (for example, if multiple values are selected or if no selection is made at all). This means that if the user hasn't specified a particular forecast adjustment, the measure will simply return 0.

4. **What It Achieves**: Overall, this expression calculates the current forecast adjustment value based on user selection. If a user selects a specific adjustment, it retrieves that value. If no specific adjustment is selected, it defaults to 0. This is useful for ensuring that calculations or visualizations based on this measure can handle cases where no specific adjustment is made, preventing errors or misleading results.

In summary, this DAX expression helps in dynamically capturing the forecast adjustment value based on user input, ensuring that the analysis remains robust and informative.

---

#### <a name="table-owners"></a>Table: `Owners`

The 'Owners' table serves to track the ownership and management structure within the organization, detailing each owner's identity alongside their respective manager and system user identifiers. This information is crucial for understanding accountability and facilitating effective communication across teams.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Manager` | `string` | The 'Manager' column identifies the individual responsible for overseeing the operations and performance of each owner listed in the Owners table. |
| `Owner` | `string` | The 'Owner' column contains the names of individuals or entities responsible for managing or overseeing the associated records within the Owners table. |
| `systemuserid` | `string` | The 'systemuserid' column stores the unique identifier for each owner in the Owners table, facilitating the association of data records with specific users in the system. |
| `SystemUserSeq` | `int64` | Column Description: The 'SystemUserSeq' column (int64) uniquely identifies each system user associated with the owners in the database, facilitating efficient data management and user tracking. |

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
   - The first part of the code calculates the total value of sales opportunities that are currently "Open" and have a sales stage that is at least 2 (indicating they are further along in the sales process).
   - It uses the `SUMX` function to sum up the values of these opportunities, which gives us a measure of potential revenue that could be realized if these opportunities are successfully closed.

2. **Base Goal Calculation**:
   - The next step is to calculate a "Base Goal" for revenue. This is done by taking the total revenue that has already been won (`Revenue Won`) and adding 60% of the revenue in the pipeline calculated earlier.
   - The result is then rounded to the nearest million using the `MROUND` function, which helps in setting a more manageable and strategic revenue target.

3. **Return the Final Goal**:
   - Finally, the code checks if the calculated `Base Goal` is greater than zero. If it is, that value is returned as the measure for the revenue goal.
   - If the `Base Goal` is not greater than zero, it defaults to rounding the same calculation to the nearest hundred thousand instead.

### Summary:
In summary, this DAX measure calculates a revenue goal by considering both the revenue already won and a portion of the potential revenue from open sales opportunities. It ensures that the goal is presented in a rounded format for easier interpretation and strategic planning. The end result is a clear target for revenue that the business aims to achieve, based on current sales activity.

---

#### <a name="table-products"></a>Table: `Products`

The 'Products' table serves as a comprehensive inventory catalog, detailing each product's unique identifier, sequence number, and associated category, enabling businesses to efficiently manage and analyze their product offerings for improved sales strategies and inventory control.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Product` | `string` | The 'Product' column contains the names of items available for sale, serving as a key identifier for inventory management and sales tracking within the Products table. |
| `Product Category` | `string` | Column Description: This column categorizes each product into specific groups, facilitating easier analysis and reporting of product performance and inventory management. |
| `ProductSeq` | `int64` | Column Description: The 'ProductSeq' column serves as a unique sequential identifier for each product in the 'Products' table, facilitating efficient data retrieval and management. |

---

#### <a name="table-territories"></a>Table: `Territories`

The 'Territories' table provides a structured overview of geographical divisions within a business's operational landscape, detailing regions, countries, and states or provinces. This data is essential for analyzing market coverage, sales performance, and resource allocation across different territories.

##### Columns

| Name | Data Type | Description (Generated) |
|------|-----------|-------------------------|
| `Country` | `string` | The 'Country' column identifies the specific nation associated with each territory, facilitating geographic categorization and data enrichment processes. |
| `Region` | `string` | The 'Region' column identifies the geographical area associated with each territory, facilitating targeted analysis and reporting of regional performance and demographics. |
| `State Or Province` | `string` | The 'State Or Province' column captures the specific administrative region within a country, facilitating the categorization and analysis of territories for enhanced data insights. |
| `Territory` | `string` | The 'Territory' column contains string values that represent distinct geographical regions or areas assigned for sales or operational purposes within the organization. |
| `TerritorySeq` | `string` | The 'TerritorySeq' column stores unique string identifiers for each territory, facilitating efficient tracking and management of territorial data within the Territories table. |

---

## <a name="report-structure"></a>Report Structure

_No report-level filters found._

### <a name="report-pages"></a>Report Pages

#### <a name="page-days-to-close-insights"></a>Page: Days to Close Insights

*Internal Name: `ReportSectionf0c8ef19be5e8127c627`, Ordinal: 6*

##### Page Level Filters

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: This Power BI filter definition is designed to focus on the `Status` of opportunities within a dataset. Here's a breakdown of what this filter does in simple business terms:

1. **Target Data**: The filter is applied to the `Opportunities` entity, specifically looking at the `Status` field of each opportunity.

2. **Included Statuses**: The filter specifies that only opportunities with a `Status` of either **'Lost'** or **'Won'** should be included in the analysis. 

3. **Exclusion of Other Statuses**: Any opportunities that have a `Status` other than 'Lost' or 'Won' will be excluded from the results. This means that statuses like 'Pending', 'In Progress', or any other status not mentioned will not be considered in the filtered data.

In summary, when this filter is applied, you will only see opportunities that are either marked as 'Lost' or 'Won', allowing for focused analysis on these specific outcomes.)
- Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Definition: N/A)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)
- Filter on `Industries`.`Industry` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)

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
  - Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
  - Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
  - Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
  - Filter on `Accounts`.`State or Province` (Type: Categorical, Definition: N/A)
  - Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)
  - Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Definition: N/A)

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

- Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to refine the data displayed in the `Opportunity Calendar` based on the `RELATIVE MONTH` field. Let's break down what this filter is doing in simple business terms:

1. **Target Data**: The filter is applied to the `RELATIVE MONTH` column in the `Opportunity Calendar` table. This column likely represents the month relative to the current date (e.g., -1 for last month, -2 for two months ago, etc.).

2. **Inclusion Criteria**: The filter includes data where the `RELATIVE MONTH` is greater than or equal to -18. This means it will show data from the last 18 months, starting from the current month. For example, if today is October 2023, the filter will include data from May 2022 onward.

3. **Exclusion Criteria**: The filter also excludes any records where the `RELATIVE MONTH` is null. This means that if there are any entries in the `Opportunity Calendar` that do not have a specified month (i.e., the month is missing), those entries will not be included in the results.

### Summary:
In summary, this filter will display all opportunities from the last 18 months (from the current month) while ensuring that any records without a specified month are excluded. This helps in focusing on relevant and complete data for analysis.)
- Filter on `Opportunities`.`Sales Stage` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Industries`.`Industry` (Type: Advanced, Definition: N/A)
- Filter on `Industries`.`IndustrySeq` (Type: Advanced, Explanation: This Power BI filter definition is designed to control which records from the `Industries` table are included in your analysis based on the `IndustrySeq` field. Let's break it down in simple business terms:

### What the Filter Does:

1. **Target Field**: The filter specifically targets the `IndustrySeq` column in the `Industries` table.

2. **Inclusion Criteria**:
   - The filter includes records where the `IndustrySeq` is **not equal to 0**.
   - It also includes records where the `IndustrySeq` is **not null** (meaning it has a valid value).

### What the Filter Excludes:

- Any record where `IndustrySeq` is **equal to 0** will be excluded from the results.
- Any record where `IndustrySeq` is **null** (meaning it has no value) will also be excluded.

### Summary:

In summary, when this filter is applied, you will only see records from the `Industries` table that have a valid `IndustrySeq` value that is neither 0 nor null. This helps ensure that your analysis focuses on meaningful data, excluding any entries that might not be relevant or valid for your reporting needs.)

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
  - Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
  - Filter on `Opportunities`.`[Opportunity Count]` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunities`.`[Revenue Won]` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to focus on a specific time frame within the "Opportunity Calendar" data, specifically the "RELATIVE MONTH" field. Let's break it down in simple business terms:

1. **Target Data**: The filter is applied to the "RELATIVE MONTH" column in the "Opportunity Calendar" table. This column likely represents a time period relative to the current date, such as "this month," "last month," or "next month."

2. **Filter Condition**: The filter is set to include only those records where the "RELATIVE MONTH" is equal to "0L." In this context, "0L" typically represents the current month. 

3. **Inclusion/Exclusion**: 
   - **Included**: Only the opportunities that fall within the current month will be included in the analysis.
   - **Excluded**: Any opportunities that are from previous months (e.g., -1 for last month) or future months (e.g., +1 for next month) will be excluded from the results.

In summary, this filter ensures that the data being analyzed only reflects opportunities that are relevant to the current month, allowing for focused reporting and insights on performance or activities happening right now.)
  - Filter on `Opportunity Calendar`.`YEAR MONTH` (Type: Categorical, Definition: N/A)

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
  - Filter on `Accounts`.`Account Name` (Type: Categorical, Definition: N/A)
  - Filter on `Opportunities`.`[Close %]` (Type: Advanced, Definition: N/A)
  - Filter on `Industries`.`Industry` (Type: TopN, Explanation: This Power BI filter definition JSON is designed to focus on specific industries based on their associated opportunities and the revenue generated from those opportunities. Here’s a breakdown of what this filter does in simple business terms:

1. **Data Sources**: The filter is working with two main data sources:
   - **Industries**: This represents different sectors or categories of businesses.
   - **Opportunities**: This refers to potential sales or business deals that have been identified.

2. **Objective**: The goal of this filter is to identify and include only the top 5 industries that have generated the highest revenue from opportunities.

3. **How It Works**:
   - **Subquery**: The filter first runs a subquery that looks at the `Opportunities` data to determine which industries are associated with the highest revenue. 
   - **Selection of Industries**: From the `Industries` table, it selects the `Industry` field.
   - **Ordering**: The results are ordered by the `Revenue Won` from the `Opportunities` table, meaning it prioritizes industries that have the most successful sales.
   - **Top 5**: It limits the results to the top 5 industries based on this revenue.

4. **Final Filter Application**: The main filter then checks the `Industries` table and includes only those industries that are part of the top 5 identified in the subquery. 

5. **Inclusion Criteria**: 
   - If an industry is among the top 5 in terms of revenue from opportunities, it will be included in the final dataset.
   - If an industry does not appear in this top 5 list, it will be excluded from the results.

In summary, this filter is used to focus on the most successful industries based on revenue generated from opportunities, ensuring that only the top performers are considered in the analysis.)
  - Filter on `Industries`.`Industry` (Type: Categorical, Definition: N/A)
  - Filter on `Opportunities`.`[Revenue Won]` (Type: Advanced, Definition: N/A)

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
  - Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to focus on a specific aspect of the data related to the "Opportunity Calendar" entity, specifically the "RELATIVE MONTH" field. Let's break it down in simple business terms:

### What the Filter Does:

1. **Target Data**: The filter is applied to the "RELATIVE MONTH" field within the "Opportunity Calendar" data. This field likely represents a time period relative to the current date, such as "this month," "last month," or "next month."

2. **Filter Condition**: The filter is set to include only those records where the "RELATIVE MONTH" is equal to **0**. In many business contexts, a value of **0** typically means "this month." 

### Inclusion and Exclusion:

- **Included Data**: Only the opportunities that are occurring in the current month will be included in the analysis. This means if you are looking at sales opportunities, only those that are relevant to the present month will be considered.

- **Excluded Data**: Any opportunities that are from previous months (e.g., -1 for last month) or future months (e.g., +1 for next month) will be excluded from the analysis. This helps in focusing solely on the current month's opportunities.

### Summary:

In summary, this filter is set up to analyze only the opportunities that are relevant to the current month, effectively excluding any data from past or future months. This is useful for businesses that want to assess their performance or activities specifically for the ongoing month.)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: This Power BI filter definition is designed to focus on the `Status` field within the `Opportunities` data. Here's a breakdown of what this filter does in simple business terms:

1. **Target Data**: The filter is applied to the `Opportunities` entity, which likely contains records of various sales opportunities your business is tracking.

2. **Filter Condition**: The filter specifically looks at the `Status` of these opportunities.

3. **Included Status**: The filter includes only those opportunities where the `Status` is marked as `'Open'`. This means that any opportunities that are closed, won, lost, or in any other status will be excluded from the data being analyzed.

In summary, when this filter is applied, you will only see opportunities that are currently open for business, allowing you to focus on active sales prospects.)
- Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
- Filter on `Opportunities`.`Opportunity Owner Name` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Industries`.`Industry` (Type: Categorical, Explanation: This Power BI filter definition is designed to control which data is included or excluded when analyzing the `Industry` field from the `Industries` table. Let's break it down in simple business terms:

1. **Target Data**: The filter is applied to the `Industry` column within the `Industries` table.

2. **Filter Logic**: The filter specifies a condition that excludes certain values from the data being analyzed. Specifically, it is looking for entries in the `Industry` column.

3. **Exclusion Criteria**: The filter states that any industry labeled as `'n/a'` should **not** be included in the results. 

4. **Resulting Data**: As a result, when this filter is applied, all industries that have the value `'n/a'` will be filtered out. This means that only industries with valid, meaningful entries (i.e., anything other than `'n/a'`) will be included in the analysis.

In summary, this filter ensures that the analysis focuses on relevant industries by excluding any entries that are marked as `'n/a'`.)

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
  - Filter on `Opportunities`.`Sum(Value)` (Type: Advanced, Definition: N/A)
  - Filter on `Accounts`.`Max(Account Name)` (Type: Advanced, Definition: N/A)
  - Filter on `Owners`.`Max(Owner)` (Type: Advanced, Definition: N/A)
  - Filter on `Products`.`Max(Product Category)` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunities`.`OpportunitySeq` (Type: Advanced, Definition: N/A)

**Pipeline by Top Industries**

- Type: `ribbonChart`
- Name: `6fe682ad2620c1cefca0`
- Fields Used:
  - `YEAR MONTH` (Query: `Opportunity Calendar.YEAR MONTH`) (Role: Category)
  - `Revenue Open` (Query: `Opportunities.Revenue Open`) (Role: Y)
  - `Industry` (Query: `Industries.Industry`) (Role: Series)
- Visual Level Filters:
  - Filter on `Accounts`.`Account Name` (Type: Categorical, Definition: N/A)
  - Filter on `Opportunities`.`[Close %]` (Type: Advanced, Definition: N/A)
  - Filter on `Industries`.`Industry` (Type: TopN, Explanation: This Power BI filter definition JSON is designed to focus on specific industries based on their associated opportunities and revenue. Here’s a breakdown of what this filter does in simple business terms:

1. **Data Sources**: The filter pulls data from two main sources:
   - **Industries**: This represents different sectors or categories of businesses.
   - **Opportunities**: This refers to potential sales or business deals associated with those industries.

2. **Selecting Industries**: The filter is set up to identify the top 5 industries based on the revenue generated from opportunities. This means it looks at the revenue figures associated with each industry and selects the five industries that have the highest revenue.

3. **Filtering Logic**:
   - The filter checks the `Industry` field from the `Industries` data.
   - It only includes those industries that are part of the top 5 identified in the previous step.

4. **Outcome**: When this filter is applied to the `Industries`.`Industry`, it effectively narrows down the data to only include the top 5 industries that are generating the most revenue from opportunities. Any industry that does not fall within this top 5 list will be excluded from the analysis.

In summary, this filter helps focus on the most financially successful industries by filtering out all others, allowing for targeted analysis and insights into high-performing sectors.)

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

- Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Definition: N/A)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)
- Filter on `Industries`.`Industry` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: This Power BI filter definition is designed to focus on the `Status` field within the `Opportunities` data. Here's a breakdown of what this filter does in simple business terms:

1. **Target Data**: The filter is applied to the `Opportunities` entity, which likely contains records of sales opportunities within a business.

2. **Filter Condition**: The filter specifically looks at the `Status` of these opportunities.

3. **Included Status**: The filter includes only those opportunities where the `Status` is marked as `'Won'`. This means that any opportunity that has been successfully closed and resulted in a sale will be included in the analysis.

4. **Excluded Status**: Conversely, any opportunities that are not marked as `'Won'` (such as those that are still open, lost, or in any other status) will be excluded from the results.

In summary, when this filter is applied, you will only see opportunities that have been successfully won, allowing for focused analysis on successful sales outcomes.)
- Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Definition: N/A)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)
- Filter on `Industries`.`Industry` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)

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
  - Filter on (Name: `Filter9eafa29b773622144b40`) (Type: Exclude, Explanation: This Power BI filter definition is designed to control which data from the "Campaigns" entity is included in a report or visualization. Let's break it down in simple business terms:

1. **Source of Data**: The filter is applied to a data source called "Campaigns," which is represented by the variable "c." This means that the filter will affect the data coming from the Campaigns table.

2. **Filter Condition**: The main condition of this filter is to **exclude** certain data. Specifically, it is looking at a column named "Campaign" within the Campaigns entity.

3. **Exclusion Criteria**: The filter is set to exclude any records where the "Campaign" column has a value of **null**. In business terms, this means that any campaign that does not have a specified name or identifier (i.e., it is missing or undefined) will not be included in the results.

### Summary:
When this filter is applied, it will only include campaigns that have a valid name or identifier. Any campaign that is missing this information (null) will be excluded from the analysis or report. This helps ensure that the data being analyzed is complete and relevant, focusing only on campaigns that can be identified.)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: This Power BI filter definition is designed to control which records from the `Opportunities` dataset are included in your analysis based on the `Status` of each opportunity.

### Breakdown of the Filter:

1. **Target Entity**: The filter is applied to the `Opportunities` entity, which likely contains various records of sales opportunities.

2. **Filter Condition**: The key part of this filter is the condition specified in the `Where` clause. It states that we want to **exclude** certain records based on their `Status`.

3. **Exclusion Criteria**: Specifically, the filter is set to exclude any opportunities that have a `Status` of **'Lost'**. 

### In Simple Terms:

- **Included Data**: This filter will include all opportunities that are **not** marked as 'Lost'. This means you will see opportunities that are still active, won, or in any other status except for 'Lost'.

- **Excluded Data**: Any opportunity that has a `Status` of 'Lost' will be filtered out and will not appear in your report or analysis.

### Summary:

When this filter is applied, you will only see opportunities that are still viable for your business, helping you focus on potential sales rather than those that have already been lost.)
- Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Definition: N/A)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)
- Filter on `Industries`.`Industry` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)

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
  - Filter on `Opportunities`.`Status` (Type: Categorical, Definition: N/A)
  - Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
  - Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
  - Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
  - Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
  - Filter on `Industries`.`Industry` (Type: Categorical, Definition: N/A)
  - Filter on `Accounts`.`State or Province` (Type: Categorical, Definition: N/A)
  - Filter on `Territories`.`Region` (Type: Categorical, Definition: N/A)
  - Filter on `Territories`.`Territory` (Type: Categorical, Definition: N/A)
  - Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)
  - Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Definition: N/A)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: This Power BI filter definition is designed to focus on specific statuses of opportunities within a business context. Here's a breakdown of what this filter does in simple terms:

1. **Target Data**: The filter is applied to the `Opportunities` entity, specifically looking at the `Status` field of each opportunity.

2. **Included Statuses**: The filter specifies that only opportunities with a `Status` of either **"Open"** or **"Won"** should be included in the analysis. 

3. **Exclusion of Other Statuses**: Any opportunities that have a `Status` other than "Open" or "Won" will be excluded from the data being analyzed. This means that statuses like "Closed", "Lost", or any other status not mentioned will not be considered.

In summary, when this filter is applied, the analysis will only reflect opportunities that are currently active (Open) or have been successfully completed (Won), allowing stakeholders to focus on these key areas of the business.)
- Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to include specific data from the "Opportunity Calendar" based on the "RELATIVE MONTH" field. Let's break it down into simpler business terms:

1. **Target Data**: The filter is applied to the "RELATIVE MONTH" column in the "Opportunity Calendar" table. This column likely represents a time frame relative to the current date (e.g., months before or after the current month).

2. **Inclusion Criteria**:
   - The filter specifies that we want to include records where the "RELATIVE MONTH" is greater than or equal to **-6**. This means we are looking for opportunities that occurred in the last 6 months leading up to the current month. For example, if the current month is October, we would include data from April to October.
   
3. **Exclusion Criteria**:
   - Additionally, the filter excludes any records where the "RELATIVE MONTH" is **null**. This means that if there are any entries in the "Opportunity Calendar" that do not have a value for "RELATIVE MONTH," those entries will not be included in the results.

### Summary:
In summary, this filter will include all opportunities from the last 6 months (up to the current month) while excluding any opportunities that do not have a defined month (null values). This helps ensure that the analysis focuses on relevant and complete data for the specified time frame.)
- Filter on `Opportunities`.`Sales Stage` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)

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
  - Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: This Power BI filter definition JSON is designed to focus on the `Status` field of the `Opportunities` entity. Here's a breakdown of what this filter does in simple business terms:

1. **Target Data**: The filter is specifically applied to the `Status` of opportunities. This means it is looking at the current state or condition of various sales opportunities in the dataset.

2. **Inclusion Criteria**: The filter is set to include only those opportunities that have a `Status` of "Open". This means that any opportunity that is currently active and not yet closed or won will be included in the analysis.

3. **Exclusion Criteria**: Conversely, any opportunities that have a `Status` of anything other than "Open" (such as "Closed", "Won", or "Lost") will be excluded from the data being analyzed. 

In summary, when this filter is applied, it narrows down the dataset to only show opportunities that are still active and available for follow-up or further action, allowing users to focus on current sales prospects.)

**Revenue Won and Revenue In Pipeline by Product LOB**

- Type: `barChart`
- Name: `90b98cca54dd8f762bb3`
- Fields Used:
  - `Product Category` (Query: `Products.Product LOB`) (Role: Category)
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Y)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Y)
  - `Product` (Query: `Products.Product`) (Role: Category)
- Visual Level Filters:
  - Filter on `Owners`.`[Rev Goal]` (Type: Advanced, Explanation: This Power BI filter definition JSON is designed to apply a specific condition to the data related to the `Rev Goal` (Revenue Goal) for the `Owners` entity. Here’s a breakdown of what this filter does in simple business terms:

1. **Target Data**: The filter is focused on the `Rev Goal` measure from the `Owners` entity. This measure represents the revenue goals set for different owners in your dataset.

2. **Condition Applied**: The filter includes a condition that compares the `Rev Goal` measure to a specific value. In this case, it is checking if the `Rev Goal` is greater than `0M` (zero million).

3. **Inclusion Criteria**: 
   - Only those records (owners) whose `Rev Goal` is greater than zero will be included in the analysis. This means that any owner with a revenue goal of zero or less will be excluded from the results.

4. **Business Implication**: By applying this filter, you are effectively focusing on owners who have set a positive revenue goal. This can help in analyzing performance, setting targets, or making strategic decisions based on owners who are actively aiming to generate revenue.

In summary, this filter ensures that only owners with a revenue goal greater than zero are considered in any reports or visualizations that utilize this filter, allowing for a more targeted analysis of performance against revenue objectives.)

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
  - Filter on `Owners`.`[Rev Goal]` (Type: Advanced, Explanation: This Power BI filter definition JSON is designed to apply a specific condition to the data related to the "Rev Goal" (Revenue Goal) for the "Owners" entity. Let's break it down in simple business terms:

1. **Target Data**: The filter is focused on the "Rev Goal" measure from the "Owners" dataset. This measure represents the revenue goals set for different owners.

2. **Filter Condition**: The filter specifies a condition that compares the "Rev Goal" value to a specific threshold. In this case, the threshold is "0M" (zero million).

3. **Inclusion/Exclusion**: 
   - The filter includes only those records where the "Rev Goal" is greater than 0 million. 
   - This means that any owner with a revenue goal of zero or less will be excluded from the data being analyzed.

In summary, when this filter is applied, it ensures that only owners with a positive revenue goal are considered in the analysis, effectively filtering out any owners who do not have a revenue target set or whose targets are negative.)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: This Power BI filter definition is designed to focus on specific statuses of opportunities within a business context. Here's a breakdown of what this filter does in simple terms:

### What the Filter Does:
- **Target Data**: The filter is applied to the `Status` field of the `Opportunities` entity, which represents different stages or outcomes of sales opportunities in a business.
  
### Included Data:
- The filter specifically includes opportunities that have a `Status` of:
  - **Open**: This means the opportunity is still active and has not yet been closed.
  - **Won**: This indicates that the opportunity has been successfully converted into a sale.

### Excluded Data:
- Any opportunities that have a `Status` other than "Open" or "Won" will be excluded from the analysis. This means that opportunities that are:
  - Closed (Lost)
  - Cancelled
  - Any other status not specified in the filter

### Summary:
In summary, when this filter is applied, the report or visualization will only show opportunities that are either still active (Open) or have been successfully closed as sales (Won). This helps users focus on the most relevant opportunities for analysis, ignoring those that are no longer active or have not resulted in a sale.)
- Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to include specific data from the `Opportunity Calendar` based on the `RELATIVE MONTH` field. Let's break it down into simpler business terms:

1. **Target Data**: The filter is applied to the `RELATIVE MONTH` field in the `Opportunity Calendar` entity. This field likely represents a time period relative to the current date (e.g., months before or after today).

2. **Inclusion Criteria**:
   - The filter includes records where the `RELATIVE MONTH` is greater than or equal to **-6**. This means it will include data from the last 6 months leading up to the current month. For example, if today is October 2023, it will include data from May 2023 to October 2023.
   
3. **Exclusion Criteria**:
   - The filter also excludes any records where the `RELATIVE MONTH` is **null**. This means that if there are any entries in the `Opportunity Calendar` that do not have a defined `RELATIVE MONTH`, those entries will not be included in the results.

### Summary:
In summary, this filter will include all opportunities from the last 6 months (up to the current month) while ensuring that any opportunities without a specified month are excluded. This helps in analyzing recent opportunities effectively while maintaining data quality by filtering out incomplete records.)
- Filter on `Opportunities`.`Sales Stage` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)

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

- Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to focus on a specific range of data from the "Opportunity Calendar" based on the "RELATIVE MONTH" field. Let's break it down in simple business terms:

### What the Filter Does:

1. **Target Data**: The filter is applied to the "RELATIVE MONTH" column in the "Opportunity Calendar" table. This column likely represents time periods relative to the current date (e.g., months in the past or future).

2. **Inclusion Criteria**: The filter specifies a range of months:
   - It includes data where the "RELATIVE MONTH" is greater than or equal to -16. This means it includes data from 16 months ago up to the present month.
   - It also includes data where the "RELATIVE MONTH" is less than or equal to 0. This means it includes data up to the current month.

### Summary of Included Data:
- The filter effectively includes all data from **16 months ago** up to **the current month**. 

### Excluded Data:
- Any data that falls outside this range is excluded. This means:
   - Data older than 16 months ago (e.g., 17 months ago or earlier) is not included.
   - Data from future months (e.g., 1 month from now or later) is also not included.

### Conclusion:
In summary, this filter is used to analyze opportunities that have occurred from 16 months ago up to the present month, allowing for a focused view of recent historical data without including any future or overly distant past data.)
- Filter on `Opportunities`.`Sales Stage` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)

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
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to focus on a specific time frame within the 'Opportunity Calendar' data, specifically the `RELATIVE MONTH` field. Let's break it down in simple business terms:

1. **Target Data**: The filter is applied to the `RELATIVE MONTH` column in the 'Opportunity Calendar' table. This column likely represents a time period relative to the current date, such as "this month," "last month," or "next month."

2. **Filter Condition**: The filter is set to include only those records where the `RELATIVE MONTH` is greater than or equal to -12. In practical terms, this means:
   - The filter is looking back 12 months from the current date.
   - It will include all data from the current month and the previous 11 months.

3. **Exclusion**: Any records that fall outside this range (i.e., older than 12 months from the current date) will be excluded from the analysis. 

In summary, this filter is used to analyze opportunities that have occurred in the last 12 months, ensuring that only relevant, recent data is considered for reporting or analysis.)

**Value In Pipeline**

- Type: `kpi`
- Name: `3562065fddd9c2eb3aa5`
- Fields Used:
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Indicator)
  - `RELATIVE MONTH` (Query: `Opportunity Calendar.RELATIVE MONTH`) (Role: TrendLine)
- Visual Level Filters:
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to focus on a specific time frame within the "Opportunity Calendar" data, specifically the "RELATIVE MONTH" field. Let's break it down in simple business terms:

1. **Target Data**: The filter is applied to the "RELATIVE MONTH" column in the "Opportunity Calendar" table. This column likely represents a time period relative to the current date, such as months before or after today.

2. **Filter Condition**: The filter is set to include only those records where the "RELATIVE MONTH" is greater than -16. In practical terms, this means:
   - The filter is looking for opportunities that are from the last 16 months or more recent. 
   - For example, if today is October 2023, the filter will include data from October 2022 (which is -12 months) up to the current month (October 2023, which is 0 months).

3. **Exclusion**: Any opportunities that are older than 16 months (i.e., those with a "RELATIVE MONTH" value of -17 or lower) will be excluded from the data set. 

In summary, this filter ensures that only opportunities from the last 16 months up to the current month are included in the analysis, allowing users to focus on more recent and relevant data.)

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
  - Filter on `Opportunities`.`[Close %]` (Type: Advanced, Definition: N/A)
  - Filter on `Accounts`.`Max(Account Name)` (Type: Advanced, Definition: N/A)
  - Filter on `Owners`.`Max(Owner)` (Type: Advanced, Definition: N/A)
  - Filter on `Products`.`Max(Product Category)` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunities`.`OpportunitySeq` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to focus on a specific time frame in the "Opportunity Calendar" data, specifically the "RELATIVE MONTH" field. Let's break it down in simple business terms:

### What the Filter Does:

1. **Target Data**: The filter is applied to the "RELATIVE MONTH" column in the "Opportunity Calendar" entity. This column likely represents a time period relative to the current date (e.g., current month, last month, next month).

2. **Inclusion Criteria**: The filter is set to include only those records where the "RELATIVE MONTH" is equal to **0**. In many business contexts, this would mean that the filter is focusing on the current month.

3. **Exclusion Criteria**: Since the filter is strictly looking for "RELATIVE MONTH" equal to 0, it effectively excludes any records that fall outside of this time frame. This means:
   - Records from the previous month (e.g., -1)
   - Records from the next month (e.g., +1)
   - Any other months (e.g., -2, +2, etc.)

### Summary:

In summary, this filter is set up to only include data from the current month in the "Opportunity Calendar." All other months, whether past or future, are excluded from the analysis. This allows users to focus specifically on opportunities that are relevant to the present month, making it easier to analyze current performance or activities.)
  - Filter on `Opportunities`.`Sum(Value)` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunity Calendar`.`YEAR MONTH` (Type: Categorical, Definition: N/A)

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
  - Filter on `Opportunities`.`Sum(Value)` (Type: Advanced, Definition: N/A)
  - Filter on `Accounts`.`Max(Account Name)` (Type: Advanced, Definition: N/A)
  - Filter on `Owners`.`Max(Owner)` (Type: Advanced, Definition: N/A)
  - Filter on `Products`.`Max(Product Category)` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunities`.`OpportunitySeq` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to focus on a specific time frame within the 'Opportunity Calendar' data, specifically the `RELATIVE MONTH` field. Here’s a breakdown of what this filter does in simple business terms:

1. **Target Data**: The filter is applied to the `RELATIVE MONTH` column in the 'Opportunity Calendar' table. This column likely represents a time period relative to the current date, such as "this month," "last month," or "next month."

2. **Filter Condition**: The filter specifies a condition that compares the `RELATIVE MONTH` value to a specific number, which in this case is `-20L`. The `-20L` indicates a relative month that is 20 months in the past from the current date.

3. **Inclusion/Exclusion of Data**: 
   - **Included Data**: The filter will include only those records from the 'Opportunity Calendar' where the `RELATIVE MONTH` is equal to `-20L`. This means it will show data specifically from 20 months ago.
   - **Excluded Data**: Any records that do not match this condition (i.e., any records from months other than 20 months ago) will be excluded from the analysis.

In summary, when this filter is applied, it narrows down the data to only include opportunities that occurred exactly 20 months ago, allowing analysts to focus on that specific time period for reporting or analysis.)

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
  - Filter on `Opportunities`.`Sum(Value)` (Type: Advanced, Definition: N/A)
  - Filter on `Accounts`.`Max(Account Name)` (Type: Advanced, Definition: N/A)
  - Filter on `Owners`.`Max(Owner)` (Type: Advanced, Definition: N/A)
  - Filter on `Products`.`Max(Product Category)` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunities`.`OpportunitySeq` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to focus on a specific aspect of the data related to the "Opportunity Calendar" entity, specifically the "RELATIVE MONTH" field. Let's break it down in simple business terms:

1. **Target Data**: The filter is applied to the "RELATIVE MONTH" column in the "Opportunity Calendar" data. This column likely represents a time frame in relation to the current date, such as months before or after the present.

2. **Filter Condition**: The filter is set to include only those records where the "RELATIVE MONTH" value is less than -20. In practical terms, this means:
   - The filter is looking for opportunities that occurred more than 20 months ago from the current date.
   - For example, if today is October 2023, the filter would include opportunities from February 2022 and earlier.

3. **Exclusion of Recent Data**: As a result of this filter, any opportunities that are from the last 20 months (i.e., from March 2022 to the present) will be excluded from the analysis.

In summary, this filter is used to analyze historical opportunities that are older than 20 months, allowing users to focus on long-term trends or outcomes rather than recent activity.)

**lineChart**

- Type: `lineChart`
- Name: `c2d8c28b154bc6a841e2`
- Fields Used:
  - `Revenue Won` (Query: `Opportunities.Revenue Won`) (Role: Y)
  - `YEAR MONTH` (Query: `Opportunity Calendar.YEAR MONTH`) (Role: Category)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Unknown)
- Visual Level Filters:
  - Filter on `Opportunities`.`Sum(Value)` (Type: Advanced, Definition: N/A)
  - Filter on `Accounts`.`Max(Account Name)` (Type: Advanced, Definition: N/A)
  - Filter on `Owners`.`Max(Owner)` (Type: Advanced, Definition: N/A)
  - Filter on `Products`.`Max(Product Category)` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunities`.`OpportunitySeq` (Type: Advanced, Definition: N/A)
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to focus on a specific time frame within the "Opportunity Calendar" data, specifically targeting the `RELATIVE MONTH` field. Let's break it down in simple business terms:

### What the Filter Does:

1. **Target Data**: The filter is applied to the `RELATIVE MONTH` column in the "Opportunity Calendar" entity. This column likely represents the month relative to the current date (e.g., current month = 0, previous month = -1, next month = 1).

2. **Inclusion Criteria**: The filter specifies that we want to include data where the `RELATIVE MONTH` is equal to **0**. This means we are focusing on opportunities that are occurring in the current month.

3. **Exclusion Criteria**: The filter does not explicitly exclude any months, but by only including data where `RELATIVE MONTH` is **0**, it effectively excludes all other months (e.g., previous months, future months).

### Summary:

In summary, this filter is set up to only include opportunities that are happening in the current month, while excluding any opportunities from previous or future months. This allows users to analyze and report on the performance and activities related to opportunities that are relevant to the present time frame.)

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

- Filter on `Opportunities`.`Status` (Type: Categorical, Explanation: This Power BI filter definition is designed to focus on the `Status` of opportunities within a dataset. Here's a breakdown of what this filter does in simple business terms:

1. **Target Data**: The filter is applied to the `Opportunities` entity, specifically looking at the `Status` field of each opportunity.

2. **Included Statuses**: The filter specifies that only opportunities with a `Status` of either **'Lost'** or **'Won'** should be included in the analysis. 

3. **Exclusion of Other Statuses**: Any opportunities that have a `Status` other than 'Lost' or 'Won' will be excluded from the results. This means that statuses like 'Pending', 'In Progress', or any other status not mentioned will not be considered in the filtered data.

In summary, when this filter is applied, the analysis will only reflect opportunities that have been marked as either 'Lost' or 'Won', allowing for focused insights on these specific outcomes.)
- Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Definition: N/A)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)
- Filter on `Industries`.`Industry` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
- Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)

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
  - Filter on `Opportunities`.`Status` (Type: Categorical, Definition: N/A)
  - Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
  - Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
  - Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
  - Filter on `Owners`.`Manager` (Type: Categorical, Definition: N/A)
  - Filter on `Accounts`.`State or Province` (Type: Categorical, Definition: N/A)
  - Filter on `Territories`.`Region` (Type: Categorical, Definition: N/A)
  - Filter on `Territories`.`Territory` (Type: Categorical, Definition: N/A)
  - Filter on `Opportunities`.`Purchase Process` (Type: Categorical, Definition: N/A)
  - Filter on `Opportunities`.`Decision Maker Identified` (Type: Categorical, Definition: N/A)

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

- Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to include specific data from the "Opportunity Calendar" based on the "RELATIVE MONTH" field. Let's break it down into simpler business terms:

1. **Target Data**: The filter is applied to the "RELATIVE MONTH" column in the "Opportunity Calendar" table. This column likely represents a time period relative to the current date (e.g., months before or after today).

2. **Inclusion Criteria**:
   - The filter includes data where the "RELATIVE MONTH" is greater than or equal to -8. This means it will include records from the last 8 months leading up to the current month. For example, if today is October 2023, it will include data from January 2023 to October 2023.
   
3. **Exclusion Criteria**:
   - The filter also excludes any records where the "RELATIVE MONTH" is null. This means that if there are any records that do not have a value for "RELATIVE MONTH," those records will not be included in the results.

### Summary:
In summary, this filter will include all opportunities from the last 8 months (up to the current month) while excluding any opportunities that do not have a specified month (null values). This helps ensure that the analysis focuses on relevant and complete data for the specified time frame.)
- Filter on `Opportunities`.`Sales Stage` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)
- Filter on `Owners`.`Owner` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product` (Type: Categorical, Definition: N/A)
- Filter on `Products`.`Product Category` (Type: Categorical, Definition: N/A)

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
  - Filter on `Owners`.`[Rev Goal]` (Type: Advanced, Explanation: This Power BI filter definition is designed to focus on the revenue goals set for owners in a business context. Let's break it down in simple terms:

1. **Target Data**: The filter is applied to the `Rev Goal` (Revenue Goal) of the `Owners` entity. This means we are specifically looking at the revenue goals that have been established for different owners in the dataset.

2. **Filter Condition**: The filter is set to include only those owners whose revenue goal is greater than zero. In other words, it is excluding any owners who have a revenue goal of zero or less.

3. **Business Implication**: By applying this filter, the analysis will focus on owners who are expected to generate revenue (those with a positive revenue goal). This can help in identifying which owners are actively contributing to the business's revenue targets and which ones are not, allowing for more targeted strategies and decisions.

In summary, this filter ensures that only owners with a revenue goal greater than zero are included in the analysis, effectively excluding any owners who do not have a revenue target to meet.)

**Closing Percentages**

- Type: `barChart`
- Name: `d6c5d8ceebb55162083f`
- Fields Used:
  - `Product Category` (Query: `Products.Product LOB`) (Role: Category)
  - `Revenue In Pipeline` (Query: `Opportunities.Revenue In Pipeline`) (Role: Tooltips)
  - `Product` (Query: `Products.Product`) (Role: Category)
  - `Close %` (Query: `Opportunities.Close %`) (Role: Y)
- Visual Level Filters:
  - Filter on `Owners`.`[Rev Goal]` (Type: Advanced, Explanation: This Power BI filter definition JSON is designed to apply a specific condition to the data related to the `Rev Goal` (Revenue Goal) for the `Owners` entity. Let's break it down in simple business terms:

1. **Target Data**: The filter is focused on the `Rev Goal` measure from the `Owners` data set. This measure typically represents the revenue targets set for different owners or entities.

2. **Filter Condition**: The filter specifies a condition that compares the `Rev Goal` value to a specific threshold. In this case, the threshold is set to "0M" (zero million).

3. **What Data is Included or Excluded**:
   - **Included**: The filter will include only those records from the `Owners` entity where the `Rev Goal` is greater than 0 million. This means that any owner with a revenue goal that is positive (greater than zero) will be included in the analysis.
   - **Excluded**: Conversely, any owner whose `Rev Goal` is 0 million or less will be excluded from the results. This helps to focus the analysis on owners who have set a revenue target that is expected to generate income.

In summary, this filter is used to ensure that only owners with a positive revenue goal are considered in the analysis, allowing for a more targeted view of performance and expectations related to revenue generation.)

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
  - Filter on `Opportunity Calendar`.`RELATIVE MONTH` (Type: Advanced, Explanation: This Power BI filter definition is designed to focus on a specific time frame within the 'Opportunity Calendar' data, specifically targeting the 'RELATIVE MONTH' field. Let's break it down in simple business terms:

1. **Target Data**: The filter is applied to the 'RELATIVE MONTH' column in the 'Opportunity Calendar' table. This column likely represents a time period relative to the current date, such as "this month," "last month," or "next month."

2. **Filter Condition**: The filter is set to include only those records where the 'RELATIVE MONTH' is equal to "0L." In this context, "0L" typically represents the current month. 

3. **Inclusion/Exclusion**: 
   - **Included**: Only the opportunities that fall within the current month will be included in the analysis.
   - **Excluded**: Any opportunities that are from previous months (e.g., -1 for last month) or future months (e.g., +1 for next month) will be excluded from the data set.

In summary, this filter is used to isolate and analyze only the opportunities that are relevant to the current month, allowing for focused reporting and insights on the most immediate business activities.)

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

