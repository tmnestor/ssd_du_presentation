import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 12), facecolor='white')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# Color scheme
colors = {
    'general': '#4A90E2',      # Blue
    'date_amount': '#F5A623',  # Orange
    'line_items': '#7ED321',   # Green
    'transaction': '#BD10E0',  # Purple
    'center': '#2C3E50'        # Dark
}

# Draw central circle
center_circle = Circle((0, 0), 0.3, facecolor=colors['center'], edgecolor='white', linewidth=3)
ax.add_patch(center_circle)
ax.text(0, 0.05, '17', fontsize=36, fontweight='bold', color='white', ha='center', va='center')
ax.text(0, -0.08, 'FIELDS', fontsize=10, color='white', ha='center', va='center')

# Define sections with their field counts
sections = [
    {'name': 'General Document\nInformation', 'count': 6, 'color': colors['general'],
     'fields': ['DOCUMENT_TYPE', 'BUSINESS_ABN', 'SUPPLIER_NAME', 'BUSINESS_ADDRESS', 'PAYER_NAME', 'PAYER_ADDRESS']},
    {'name': 'Date & Amount\nInformation', 'count': 5, 'color': colors['date_amount'],
     'fields': ['INVOICE_DATE', 'STATEMENT_DATE_RANGE', 'IS_GST_INCLUDED', 'GST_AMOUNT', 'TOTAL_AMOUNT']},
    {'name': 'Line Item\nDetails', 'count': 4, 'color': colors['line_items'],
     'fields': ['LINE_ITEM_DESCRIPTIONS', 'LINE_ITEM_QUANTITIES', 'LINE_ITEM_PRICES', 'LINE_ITEM_TOTAL_PRICES']},
    {'name': 'Transaction\nInformation', 'count': 2, 'color': colors['transaction'],
     'fields': ['TRANSACTION_DATES', 'TRANSACTION_AMOUNTS_PAID']}
]

# Calculate angles for each section
total_fields = 17
start_angle = 90

for i, section in enumerate(sections):
    # Calculate wedge size based on field count
    angle_size = (section['count'] / total_fields) * 360
    end_angle = start_angle - angle_size

    # Draw outer ring segment
    wedge = Wedge((0, 0), 1.0, start_angle, end_angle,
                  facecolor=section['color'], alpha=0.8, edgecolor='white', linewidth=3)
    ax.add_patch(wedge)

    # Draw inner ring segment (lighter shade)
    inner_wedge = Wedge((0, 0), 0.7, start_angle, end_angle,
                       facecolor=section['color'], alpha=0.3, edgecolor='white', linewidth=2)
    ax.add_patch(inner_wedge)

    # Add section label
    mid_angle = np.radians((start_angle + end_angle) / 2)
    label_r = 1.25
    label_x = label_r * np.cos(mid_angle)
    label_y = label_r * np.sin(mid_angle)

    ax.text(label_x, label_y, section['name'], fontsize=11, fontweight='bold',
            ha='center', va='center', color=section['color'])

    # Add field count
    count_r = 0.85
    count_x = count_r * np.cos(mid_angle)
    count_y = count_r * np.sin(mid_angle)

    count_circle = Circle((count_x, count_y), 0.08,
                          facecolor='white', edgecolor=section['color'], linewidth=2)
    ax.add_patch(count_circle)
    ax.text(count_x, count_y, str(section['count']), fontsize=12, fontweight='bold',
            ha='center', va='center', color=section['color'])

    start_angle = end_angle

# Add title
ax.text(0, 1.4, 'WRE Critical Fields for Substantiation',
        fontsize=18, fontweight='bold', ha='center', color=colors['center'])

# Add subtitle
ax.text(0, -1.4, 'Automated Validation • Cross-Referencing • Compliance • Audit Trail',
        fontsize=10, ha='center', color='#666666', style='italic')

plt.tight_layout()
plt.savefig('/Users/tod/Desktop/ssd_du_presentation/17_fields_circular.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("Circular infographic saved as '17_fields_circular.png'")