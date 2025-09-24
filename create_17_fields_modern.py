import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

# Set up the figure with modern gradient background
fig, ax = plt.subplots(figsize=(14, 10), facecolor='white')
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Create gradient background
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient = np.vstack((gradient, gradient))
ax.imshow(gradient, aspect='auto', cmap='Blues_r', alpha=0.1, extent=[0, 14, 0, 10])

# Modern color palette
colors = {
    'primary': '#0066CC',
    'secondary': '#FF6B35',
    'accent1': '#00D9FF',
    'accent2': '#FFD93D',
    'dark': '#1A1A2E',
    'light': '#F5F5F5'
}

# Title with modern styling
title_rect = FancyBboxPatch((1, 8.5), 12, 1.2,
                            boxstyle="round,pad=0.02",
                            facecolor=colors['dark'],
                            edgecolor='none')
ax.add_patch(title_rect)
ax.text(7, 9.1, '17 CRITICAL FIELDS', fontsize=22, fontweight='bold',
        color='white', ha='center', va='center')
ax.text(7, 8.2, 'Work-Related Expense Substantiation Requirements',
        fontsize=11, color=colors['accent1'], ha='center', va='center')

# Create card-style sections
def create_card(x, y, width, height, title, count, fields, color, icon_text):
    # Card shadow
    shadow = FancyBboxPatch((x+0.05, y-0.05), width, height,
                            boxstyle="round,pad=0.02",
                            facecolor='gray', alpha=0.2,
                            edgecolor='none')
    ax.add_patch(shadow)

    # Main card
    card = FancyBboxPatch((x, y), width, height,
                          boxstyle="round,pad=0.02",
                          facecolor='white',
                          edgecolor=color, linewidth=2)
    ax.add_patch(card)

    # Header strip
    header = Rectangle((x, y + height - 0.6), width, 0.6,
                      facecolor=color, edgecolor='none')
    ax.add_patch(header)

    # Icon circle
    icon_circle = plt.Circle((x + 0.4, y + height - 0.3), 0.15,
                            facecolor='white', edgecolor='none')
    ax.add_patch(icon_circle)
    ax.text(x + 0.4, y + height - 0.3, icon_text, fontsize=14,
            ha='center', va='center', color=color)

    # Title
    ax.text(x + 0.8, y + height - 0.3, title, fontsize=11,
            fontweight='bold', color='white', va='center')

    # Count badge
    badge = plt.Circle((x + width - 0.4, y + height - 0.3), 0.15,
                      facecolor='white', edgecolor='none')
    ax.add_patch(badge)
    ax.text(x + width - 0.4, y + height - 0.3, str(count),
            fontsize=12, fontweight='bold', ha='center', va='center', color=color)

    # Field list
    for i, field in enumerate(fields):
        y_pos = y + height - 1.1 - (i * 0.35)
        ax.text(x + 0.3, y_pos, f'• {field}', fontsize=9,
                color=colors['dark'], va='center')

# Create the four cards
create_card(0.5, 4.5, 3.2, 3.0,
           'General Document', 6,
           ['DOCUMENT_TYPE', 'BUSINESS_ABN', 'SUPPLIER_NAME',
            'BUSINESS_ADDRESS', 'PAYER_NAME', 'PAYER_ADDRESS'],
           colors['primary'], '📄')

create_card(4.0, 4.5, 3.2, 3.0,
           'Date & Amount', 5,
           ['INVOICE_DATE', 'STATEMENT_DATE', 'IS_GST_INCLUDED',
            'GST_AMOUNT', 'TOTAL_AMOUNT'],
           colors['secondary'], '📅')

create_card(7.5, 4.5, 3.2, 3.0,
           'Line Items', 4,
           ['ITEM_DESCRIPTIONS', 'ITEM_QUANTITIES',
            'ITEM_PRICES', 'ITEM_TOTAL_PRICES'],
           colors['accent1'], '📋')

create_card(11.0, 4.5, 2.5, 3.0,
           'Transactions', 2,
           ['TRANSACTION_DATES',
            'AMOUNTS_PAID'],
           colors['accent2'], '💳')

# Stats bar at bottom
stats_rect = FancyBboxPatch((0.5, 1.5), 13, 2.5,
                            boxstyle="round,pad=0.02",
                            facecolor=colors['light'],
                            edgecolor=colors['dark'], linewidth=1)
ax.add_patch(stats_rect)

# Add key benefits
benefits = [
    ('✅', 'Automated\nValidation'),
    ('🔗', 'Cross\nReferencing'),
    ('📊', 'Compliance\nChecking'),
    ('📁', 'Audit Trail\nMaintenance')
]

for i, (icon, text) in enumerate(benefits):
    x_pos = 2.5 + (i * 3)
    # Icon
    icon_bg = plt.Circle((x_pos, 3.2), 0.25,
                         facecolor=colors['primary'], alpha=0.2)
    ax.add_patch(icon_bg)
    ax.text(x_pos, 3.2, icon, fontsize=16, ha='center', va='center')
    # Text
    ax.text(x_pos, 2.5, text, fontsize=9, ha='center', va='center',
            color=colors['dark'])

# Progress indicator
ax.text(7, 0.8, 'Complete document capture ensures accurate expense substantiation',
        fontsize=10, ha='center', style='italic', color=colors['dark'])

# Add decorative elements
for i in range(3):
    circle = plt.Circle((1 + i*6, 0.3), 0.05,
                       facecolor=colors['primary'], alpha=0.3 - i*0.1)
    ax.add_patch(circle)

plt.tight_layout()
plt.savefig('/Users/tod/Desktop/ssd_du_presentation/17_fields_modern.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("Modern card-style infographic saved as '17_fields_modern.png'")