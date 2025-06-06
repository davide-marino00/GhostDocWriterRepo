# pbi_data_models.py - Updated with fields for LLM output

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Dict, Any

# --- Data Classes ---

@dataclass
class FilterTarget:
    """Represents the target of a filter expression."""
    entity: Optional[str] = None # e.g., "DimDate" [cite: 128]
    property: Optional[str] = None # e.g., "CurrentYearFlag" [cite: 128]
    # Add other potential target types if found (e.g., Measure, HierarchyLevel)

@dataclass
class ReportFilter:
    """Represents a filter applied at Report, Page, or Visual level."""
    name: Optional[str] = None # Internal name/ID [cite: 118, 129]
    filter_type: Optional[str] = None # e.g., "Advanced" [cite: 122, 133]
    level: Optional[str] = None # Added during parsing: 'Report', 'Page', 'Visual'
    target: Optional[FilterTarget] = None # Parsed from 'expression' object
    # Store the complex filter logic as raw dict for now, parsing can be complex
    filter_definition: Optional[Dict[str, Any]] = None # Raw 'filter' object [cite: 118, 129]
    # Optional field for LLM explanation later
    llm_explanation: Optional[str] = None

@dataclass
class VisualFieldMapping:
    """Represents how a data field is used in a visual role."""
    role: str # e.g., "Values", "Axis", "Legend" (from dataTransforms.json selects/DataRoles or config projections)
    query_ref: Optional[str] = None # e.g., "vw_Timesheet.MAIN_UNIT" (queryName from dataTransforms or queryRef from config) [cite: 113, 34]
    display_name: Optional[str] = None # e.g., "Unit" (from dataTransforms or columnProperties) [cite: 113, 37]
    # Could add 'type' or 'category' from dataTransforms selects if needed

@dataclass
class Visual:
    """Represents a single visual on a report page."""
    name: Optional[str] = None # Internal name/ID from config.json [cite: 33]
    visual_id: Optional[str] = None # Maybe 'id' from visualContainer.json? [cite: 32] (Type might differ)
    visual_type: Optional[str] = None # e.g., "slicer" [cite: 34]
    title: Optional[str] = None # Parsed from config.json 'objects.title.properties.text' [cite: 53]
    x: Optional[float] = None # Position from visualContainer.json [cite: 32]
    y: Optional[float] = None # Position from visualContainer.json [cite: 32]
    width: Optional[float] = None # Dimension from visualContainer.json [cite: 32]
    height: Optional[float] = None # Dimension from visualContainer.json [cite: 32]
    visual_level_filters: List[ReportFilter] = field(default_factory=list) # Parsed from visual filters.json [cite: 1]
    field_mappings: List[VisualFieldMapping] = field(default_factory=list) # Parsed from config/dataTransforms [cite: 34, 111, 113]
    # Optional field for LLM description later
    llm_description: Optional[str] = None

@dataclass
class ReportPage:
    """Represents a single page (section) in the report."""
    name: Optional[str] = None # Internal name/ID from section.json [cite: 122]
    display_name: Optional[str] = None # From section.json [cite: 122]
    ordinal: int = 0 # From section.json [cite: 122]
    width: Optional[float] = None # From section.json [cite: 122]
    height: Optional[float] = None # From section.json [cite: 122]
    page_level_filters: List[ReportFilter] = field(default_factory=list) # Parsed from page filters.json [cite: 117]
    visuals: List[Visual] = field(default_factory=list) # List of Visual objects on this page


@dataclass
class Annotation:
    """Represents a TMDL annotation."""
    name: str
    value: str # Store value as string, can be simple string or JSON string

@dataclass
class Column:
    """Represents a regular column in a table."""
    name: str
    dataType: str
    sourceColumn: Optional[str] = None # Present for regular columns
    formatString: Optional[str] = None
    isHidden: bool = False
    summarizeBy: str = 'none'
    description: Optional[str] = None # Existing description annotation
    annotations: List[Annotation] = field(default_factory=list)
    # --- Added Field for LLM Enrichment ---
    llm_description: Optional[str] = None # LLM-generated description

@dataclass
class CalculatedColumn(Column):
    """Represents a calculated column (inherits from Column, no sourceColumn)."""
    daxExpression: str = ""
    sourceColumn: Optional[str] = None # Explicitly None for calculated columns
    # --- Added Field for LLM Enrichment ---
    # llm_description is inherited from Column
    llm_dax_explanation: Optional[str] = None # LLM-generated explanation of DAX

@dataclass
class Measure:
    """Represents a measure in a table."""
    name: str
    daxExpression: str
    formatString: Optional[str] = None
    isHidden: bool = False
    description: Optional[str] = None # Existing description annotation
    annotations: List[Annotation] = field(default_factory=list)
    # --- Added Fields for LLM Enrichment ---
    llm_description: Optional[str] = None # LLM-generated description (optional use case)
    llm_dax_explanation: Optional[str] = None # LLM-generated explanation of DAX

@dataclass
class Table:
    """Represents a table with its columns and measures."""
    name: str
    isHidden: bool = False
    description: Optional[str] = None # Existing description annotation
    annotations: List[Annotation] = field(default_factory=list)
    columns: List[Column] = field(default_factory=list) # Includes regular and calculated
    measures: List[Measure] = field(default_factory=list)
    # --- Added Field for LLM Enrichment ---
    llm_description: Optional[str] = None # LLM-generated description

@dataclass
class Relationship:
    """Represents a relationship between two columns."""
    # No LLM fields added here by default, but could be if needed
    fromTable: str
    fromColumn: str
    toTable: str
    toColumn: str
    isActive: bool = True
    crossFilteringBehavior: str = 'singleDirection' # Default

# --- Helper Function for JSON Serialization ---
# Custom JSON encoder to handle dataclasses and Path objects
class DataClassEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Path):
             return str(o)
         # Check if it's one of our dataclasses (or any object with __dict__)
        if hasattr(o, '__dataclass_fields__'):
            return o.__dict__
        return super().default(o)