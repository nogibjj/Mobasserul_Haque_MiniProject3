import polars as pl
import matplotlib.pyplot as plt

file_path = "Customer Purchasing Behaviors.csv"
output_report = "summary_report.md"

def read_csv_file(path):
    return pl.read_csv(path)

def summary_statistics(dataframe, report_file):
    """Display summary statistics for numerical columns in the DataFrame."""
    summary = dataframe.describe()

    # Transpose the summary DataFrame for better readability
    summary_t = summary.transpose(include_header=True)

    with open(report_file, 'a', encoding='utf-8') as file:
        file.write("### Summary Statistics\n")
        file.write("\n| Metric | " + " | ".join(summary_t.columns) + " |\n")
        file.write("|--------|" + "------|" * len(summary_t.columns) + "\n")
        
        # Loop through summary statistics and format them in a markdown table
        for row in summary_t.to_dicts():
            row_values = [f"{row[col]}" for col in summary_t.columns]
            file.write(f"| {row['column']} | " + " | ".join(row_values) + " |\n")

        file.write("\n\n")

def plot_histograms(dataframe, columns, report_file, bins=20):
    """Plot histograms for specified columns in the DataFrame."""
    plt.figure(figsize=(12, 6))
    
    for col in columns:
        plt.hist(dataframe[col].to_numpy(), bins=bins, edgecolor='black', alpha=0.7, label=col)
    
    plt.suptitle('Distribution of age, annual income, purchase amount, and purchase frequency')
    plt.legend(loc='upper right')
    histogram_path = "Histogram_column_distributions.png"
    plt.savefig(histogram_path)

    # Add the histogram image to the markdown file
    with open(report_file, 'a', encoding='utf-8') as file:
        file.write(f"### Histograms for Selected Columns\n")
        file.write(f"![Histograms]({histogram_path})\n\n")

def plot_bar_by_category(dataframe, category_col, value_col, report_file):
    """Compare average purchase amounts by region."""
    plt.figure(figsize=(10, 6))

    # Perform group_by and explicitly name the aggregation result as 'average_value'
    avg_purchase = dataframe.group_by(category_col).agg(
        pl.col(value_col).mean().alias('average_value')
    )

    # Convert Polars columns to numpy for direct plotting
    categories = avg_purchase[category_col].to_numpy()
    values = avg_purchase['average_value'].to_numpy()  # Accessing the renamed column 'average_value'

    plt.bar(categories, values)
    
    plt.title(f'Average {value_col} by {category_col}')
    plt.xlabel(category_col)
    plt.ylabel(f'Average {value_col}')
    
    bar_plot_path = "bar_plot_average_purchase_amt_by_regions.png"
    plt.savefig(bar_plot_path)

    # Add the bar plot image to the markdown file
    with open(report_file, 'a', encoding='utf-8') as file:
        file.write(f"### Bar Plot: Average {value_col} by {category_col}\n")
        file.write(f"![Bar Plot]({bar_plot_path})\n\n")
        
# Reading the data using Polars
df = read_csv_file(file_path)

# Clear the contents of the report file to start fresh
with open(output_report, 'w', encoding='utf-8') as file:
    file.write("# Summary Report\n\n")

# Writing summary statistics to the summary report file
summary_statistics(df, output_report)

# Generating plots and saving them in the summary report file
plot_histograms(df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'], output_report)
plot_bar_by_category(df, 'region', 'purchase_amount', output_report)
