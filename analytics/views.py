from django.shortcuts import render
import pandas as pd

data = {
    "total_amount_category": {
        "image": "total_amount_category.png",
        "insight": "Total amount spent per category gives insights into top-selling categories."
    },
    "payment_distribution": {
        "image": "payment_distribution.png",
        "insight": "Payment method distribution shows customer preferences for online transactions."
    },
    "monthly_total_sales": {
        "image": "monthly_total_sales.png",
        "insight": "Sales trend over months indicates peak sales periods and seasonal variations."
    },
    "customer_clv_segments": {
        "image": "customer_clv_segments.png",
        "insight": "CLV segments help identify high-value customers and optimize retention strategies."
    },
    "average_clv_location": {
        "image": "average_clv_location.png",
        "insight": "Stores with higher average CLV can be targeted for premium offerings."
    },
    "total_sales_location": {
        "image": "total_sales_location.png",
        "insight": "Total sales by store location highlight the best-performing branches."
    },
    "customer_segmentation": {
        "image": "customer_segmentation.png",
        "insight": "KMeans clustering groups customers based on spending habits."
    },
    "active_vs_churned": {
        "image": "active_vs_churned.png",
        "insight": "Proportion of active vs churned customers helps in designing loyalty programs."
    },
    "repeat_purchase_rate": {
        "image": "repeat_purchase_rate.png",
        "insight": "Repeat purchase rate shows customer retention trends."
    },
    "cohort_churn_analysis": {
        "image": "cohort_churn_analysis.png",
        "insight": "Cohort-based churn analysis identifies customer lifecycle patterns."
    },
}

# Load dataset
df = pd.read_csv("Retail_Transaction_Dataset.csv")

# Get dataset details
dataset_info = {
    "rows": df.shape[0],
    "columns": df.shape[1],
    "columns_list": list(df.columns),
    "missing_values": df.isnull().sum().to_dict(),  # Missing values per column
    "first_five_rows": df.head().to_html(classes="table table-bordered")  # Convert to HTML table
}

# Home Page View
def home(request):
    formatted_charts = {key: key.replace('_', ' ').title() for key in data.keys()}
    return render(request, 'analytics/home.html', {'charts': formatted_charts, 'dataset_info': dataset_info})


# Visualization Page View
def visualization(request, chart):
    if chart in data:
        formatted_charts = {key: key.replace('_', ' ').title() for key in data.keys()}  # Format names properly
        return render(request, 'analytics/visualization.html', {
            'chart': chart,
            'chart_name': chart.replace('_', ' ').title(),  # Format selected chart title
            'chart_data': data[chart],
            'all_charts': formatted_charts  # Pass formatted chart names
        })
    else:
        return render(request, 'analytics/404.html', status=404)
    

