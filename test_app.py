import pytest
import pandas as pd
from app import create_dash_app

def test_header_present():
    # Create test data
    test_df = pd.DataFrame({
        'date': ['2021-01-01', '2021-01-02'],
        'region': ['north', 'south'],
        'sales': [100, 150]
    })
    
    # Create the app
    app = create_dash_app(test_df)
    
    # Check if header exists in layout
    header_component = None
    for component in app.layout.children:
        if hasattr(component, 'id') and component.id == 'main-header':
            header_component = component
            break
    
    assert header_component is not None, "Header component not found"
    assert header_component.children == 'Pink Morsel Sales Visualizer'

def test_visualization_present():
    test_df = pd.DataFrame({
        'date': ['2021-01-01', '2021-01-02'],
        'region': ['north', 'south'],
        'sales': [100, 150]
    })
    
    app = create_dash_app(test_df)
    
    # Check if graph exists
    graph_component = None
    for component in app.layout.children:
        if hasattr(component, 'id') and component.id == 'sales-graph':
            graph_component = component
            break
    
    assert graph_component is not None, "Graph component not found"

def test_region_picker_present():
    test_df = pd.DataFrame({
        'date': ['2021-01-01', '2021-01-02'],
        'region': ['north', 'south'],
        'sales': [100, 150]
    })
    
    app = create_dash_app(test_df)
    
    # Check if region picker exists
    radio_component = None
    for component in app.layout.children:
        if hasattr(component, 'id') and component.id == 'region-radio':
            radio_component = component
            break
    
    assert radio_component is not None, "Region radio component not found"
    assert len(radio_component.options) == 2  # Should have 2 regions