import polars as pl
import matplotlib.pyplot as plt
from io import StringIO
from main import (
    summary_statistics, plot_histograms, plot_bar_by_category
)

sample_data = """customer_id,age,annual_income,purchase_amount,purchase_frequency,region,loyalty_score
1,23,50000,200,5,North,80
2,45,60000,300,7,South,85
3,34,55000,250,6,East,90
4,50,65000,400,8,West,70
5,29,70000,350,7,North,75
"""

# Function to create Polars DataFrame from sample data using StringIO
def setup_dataframe():
    return pl.read_csv(StringIO(sample_data))

def test_summary_statistics():
    """Test summary_statistics function using Polars"""
    df = setup_dataframe()
    summary_statistics(df, "test_report.md")
    print("test_summary_statistics passed")

def test_plot_histograms():
    """Test plot_histograms function using Polars"""
    df = setup_dataframe()

    # Mock plt.show to prevent actual plotting during tests
    plt.show = lambda: None
    plot_histograms(df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'], "test_report.md")
    print("test_plot_histograms passed")

def test_plot_bar_by_category():
    """Test plot_bar_by_category function using Polars"""
    df = setup_dataframe()

    plt.show = lambda: None
    plot_bar_by_category(df, 'region', 'purchase_amount', "test_report.md")
    print("test_plot_bar_by_category passed")

# Run the tests
test_summary_statistics()
test_plot_histograms()
test_plot_bar_by_category()
