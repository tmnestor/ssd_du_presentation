import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

# Set up the figure with a clean, modern style
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(16, 10), facecolor='#f8f9fa')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Define color scheme
colors = {
    'general': '#3498db',      # Blue
    'date_amount': '#e74c3c',  # Red
    'line_items': '#2ecc71',   # Green
    'transaction': '#f39c12',  # Orange
    'background': '#ecf0f1',   # Light gray
    'header': '#2c3e50'        # Dark blue-gray
}

# Title
title_box = FancyBboxPatch((0.5, 8.8), 9, 1,
                           boxstyle="round,pad=0.1",
                           facecolor=colors['header'],
                           edgecolor='none',
                           transform=ax.transData)
ax.add_patch(title_box)
ax.text(5, 9.3, 'The 17 Critical Fields for WRE Substantiation',
        fontsize=24, fontweight='bold', color='white',
        ha='center', va='center')

# Category 1: General Document Information
cat1_y = 7.5
cat1_box = FancyBboxPatch((0.5, cat1_y - 2.2), 4.3, 2.3,
                          boxstyle="round,pad=0.05",
                          facecolor=colors['general'],
                          alpha=0.15,
                          edgecolor=colors['general'],
                          linewidth=2)
ax.add_patch(cat1_box)

ax.text(2.65, cat1_y, 'General Document Information',
        fontsize=14, fontweight='bold', color=colors['general'])
ax.text(2.65, cat1_y - 0.3, '(6 fields)',
        fontsize=11, style='italic', color=colors['general'])

fields1 = [
    '• DOCUMENT_TYPE',
    '• BUSINESS_ABN',
    '• SUPPLIER_NAME',
    '• BUSINESS_ADDRESS',
    '• PAYER_NAME',
    '• PAYER_ADDRESS'
]
for i, field in enumerate(fields1):
    ax.text(0.8, cat1_y - 0.65 - (i*0.25), field,
            fontsize=10, color='#2c3e50')

# Category 2: Date and Amount Information
cat2_y = 7.5
cat2_box = FancyBboxPatch((5.2, cat2_y - 2.2), 4.3, 2.3,
                          boxstyle="round,pad=0.05",
                          facecolor=colors['date_amount'],
                          alpha=0.15,
                          edgecolor=colors['date_amount'],
                          linewidth=2)
ax.add_patch(cat2_box)

ax.text(7.35, cat2_y, 'Date and Amount Information',
        fontsize=14, fontweight='bold', color=colors['date_amount'])
ax.text(7.35, cat2_y - 0.3, '(5 fields)',
        fontsize=11, style='italic', color=colors['date_amount'])

fields2 = [
    '• INVOICE_DATE',
    '• STATEMENT_DATE_RANGE',
    '• IS_GST_INCLUDED',
    '• GST_AMOUNT',
    '• TOTAL_AMOUNT'
]
for i, field in enumerate(fields2):
    ax.text(5.5, cat2_y - 0.65 - (i*0.25), field,
            fontsize=10, color='#2c3e50')

# Category 3: Line Item Details
cat3_y = 4.5
cat3_box = FancyBboxPatch((0.5, cat3_y - 1.7), 4.3, 1.8,
                          boxstyle="round,pad=0.05",
                          facecolor=colors['line_items'],
                          alpha=0.15,
                          edgecolor=colors['line_items'],
                          linewidth=2)
ax.add_patch(cat3_box)

ax.text(2.65, cat3_y, 'Line Item Details',
        fontsize=14, fontweight='bold', color=colors['line_items'])
ax.text(2.65, cat3_y - 0.3, '(4 fields)',
        fontsize=11, style='italic', color=colors['line_items'])

fields3 = [
    '• LINE_ITEM_DESCRIPTIONS',
    '• LINE_ITEM_QUANTITIES',
    '• LINE_ITEM_PRICES',
    '• LINE_ITEM_TOTAL_PRICES'
]
for i, field in enumerate(fields3):
    ax.text(0.8, cat3_y - 0.65 - (i*0.25), field,
            fontsize=10, color='#2c3e50')

# Category 4: Transaction Information
cat4_y = 4.5
cat4_box = FancyBboxPatch((5.2, cat4_y - 1.7), 4.3, 1.8,
                          boxstyle="round,pad=0.05",
                          facecolor=colors['transaction'],
                          alpha=0.15,
                          edgecolor=colors['transaction'],
                          linewidth=2)
ax.add_patch(cat4_box)

ax.text(7.35, cat4_y, 'Transaction Information',
        fontsize=14, fontweight='bold', color=colors['transaction'])
ax.text(7.35, cat4_y - 0.3, '(2 fields - Bank Statements only)',
        fontsize=11, style='italic', color=colors['transaction'])

fields4 = [
    '• TRANSACTION_DATES',
    '• TRANSACTION_AMOUNTS_PAID'
]
for i, field in enumerate(fields4):
    ax.text(5.5, cat4_y - 0.65 - (i*0.25), field,
            fontsize=10, color='#2c3e50')

# Add visual field count indicators
def add_field_counter(x, y, count, color):
    circle = Circle((x, y), 0.25, facecolor=color, edgecolor='white', linewidth=2)
    ax.add_patch(circle)
    ax.text(x, y, str(count), fontsize=12, fontweight='bold',
            color='white', ha='center', va='center')

add_field_counter(4.5, 6.5, 6, colors['general'])
add_field_counter(9.2, 6.5, 5, colors['date_amount'])
add_field_counter(4.5, 3.5, 4, colors['line_items'])
add_field_counter(9.2, 3.5, 2, colors['transaction'])

# Add bottom summary
summary_box = FancyBboxPatch((0.5, 0.5), 9, 1.2,
                             boxstyle="round,pad=0.1",
                             facecolor=colors['background'],
                             edgecolor=colors['header'],
                             linewidth=1)
ax.add_patch(summary_box)

ax.text(5, 1.3, '✓ Automated Validation  ✓ Cross-Referencing  ✓ Compliance Checking  ✓ Audit Trail',
        fontsize=12, color=colors['header'], ha='center', fontweight='bold')
ax.text(5, 0.8, 'These fields enable comprehensive Work-Related Expense substantiation for Australian tax compliance',
        fontsize=10, color='#34495e', ha='center', style='italic')

# Add decorative elements
for i in range(5):
    alpha = 0.05 - (i * 0.01)
    decorative = FancyBboxPatch((0.3 - i*0.05, 0.3 - i*0.05),
                                9.4 + i*0.1, 9.4 + i*0.1,
                                boxstyle="round,pad=0.02",
                                facecolor='none',
                                edgecolor=colors['header'],
                                alpha=alpha,
                                linewidth=1)
    ax.add_patch(decorative)

plt.tight_layout()
plt.savefig('/Users/tod/Desktop/ssd_du_presentation/17_critical_fields_infographic.png',
            dpi=300, bbox_inches='tight', facecolor='#f8f9fa')
plt.close()

print("Infographic saved as '17_critical_fields_infographic.png'")