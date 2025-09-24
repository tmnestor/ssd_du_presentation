import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Set up the figure with transparent background
fig, ax = plt.subplots(figsize=(20, 7), facecolor='none')
ax.set_xlim(0, 20)
ax.set_ylim(0, 7)
ax.axis('off')

# Modern color palette
colors = {
    'primary': '#0066CC',      # Blue
    'secondary': '#FF6B35',    # Orange
    'accent1': '#00D9FF',      # Cyan
    'accent2': '#FFD93D',      # Yellow
    'dark': '#1A1A2E',         # Dark blue
    'text': '#2C3E50',         # Dark gray
    'white': '#FFFFFF'
}

# Title section - expanded for both lines
title_rect = FancyBboxPatch((1, 5.5), 18, 1.3,
                            boxstyle="round,pad=0.02",
                            facecolor=colors['dark'],
                            edgecolor='none')
ax.add_patch(title_rect)
ax.text(10, 6.4, '17 CRITICAL FIELDS', fontsize=28, fontweight='bold',
        color='white', ha='center', va='center')

# Subtitle inside the header box
ax.text(10, 5.9, 'Work-Related Expense Substantiation Requirements',
        fontsize=16, color=colors['accent1'], ha='center', va='center')

# Create clean card-style sections
def create_clean_card(x, y, width, height, title, count, fields, color, icon_num):
    # Card shadow (subtle)
    shadow = FancyBboxPatch((x+0.02, y-0.02), width, height,
                            boxstyle="round,pad=0.015",
                            facecolor='#E0E0E0', alpha=0.5,
                            edgecolor='none')
    ax.add_patch(shadow)

    # Main card with colored border
    card = FancyBboxPatch((x, y), width, height,
                          boxstyle="round,pad=0.015",
                          facecolor='white',
                          edgecolor=color, linewidth=3)
    ax.add_patch(card)

    # Colored header bar
    header = FancyBboxPatch((x, y + height - 0.5), width, 0.5,
                           boxstyle="round,pad=0.01",
                           facecolor=color,
                           edgecolor='none')
    ax.add_patch(header)

    # Icon circle (left)
    icon_bg = plt.Circle((x + 0.35, y + height - 0.25), 0.15,
                         facecolor='white', edgecolor='none', zorder=10)
    ax.add_patch(icon_bg)
    ax.text(x + 0.35, y + height - 0.25, icon_num, fontsize=14, fontweight='bold',
            ha='center', va='center', color=color, zorder=11)

    # Title text - larger
    ax.text(x + 0.7, y + height - 0.25, title, fontsize=14,
            fontweight='bold', color='white', va='center')

    # Count badge (right)
    count_bg = plt.Circle((x + width - 0.35, y + height - 0.25), 0.15,
                          facecolor='white', edgecolor='none', zorder=10)
    ax.add_patch(count_bg)
    ax.text(x + width - 0.35, y + height - 0.25, str(count),
            fontsize=16, fontweight='bold', ha='center', va='center',
            color=color, zorder=11)

    # Field list with bullets - larger text
    for i, field in enumerate(fields):
        y_pos = y + height - 0.75 - (i * 0.42)  # Adjusted spacing for larger text
        # Bullet point
        bullet = plt.Circle((x + 0.2, y_pos), 0.04,
                           facecolor=color, alpha=0.7)
        ax.add_patch(bullet)
        # Split field into name and description if colon present
        if ':' in field:
            field_name, field_desc = field.split(':', 1)
            # Field name in bold - larger
            ax.text(x + 0.35, y_pos + 0.1, field_name + ':', fontsize=9,
                    color=colors['text'], va='top', ha='left', fontweight='bold')
            # Description on same/next line - larger
            ax.text(x + 0.35, y_pos - 0.1, field_desc.strip(), fontsize=8,
                    color=colors['text'], va='top', ha='left', alpha=0.85, wrap=True)
        else:
            # Field text without description
            ax.text(x + 0.35, y_pos, field, fontsize=9,
                    color=colors['text'], va='center', ha='left')

# Create the four cards with proper spacing
card_height = 4.0  # Taller cards for larger text
card_y = 1.5

# Card 1: General Document with descriptions
general_fields = [
    'DOCUMENT_TYPE: Classify as invoice, receipt, or bank statement',
    'BUSINESS_ABN: Verify legitimate Australian businesses via 11-digit ABN',
    'SUPPLIER_NAME: Identify the business providing goods/services',
    'BUSINESS_ADDRESS: Confirm business location for legitimacy checks',
    'PAYER_NAME: Match against taxpayer records',
    'PAYER_ADDRESS: Verify taxpayer identity and address consistency'
]

# Card 2: Date & Amount with descriptions
date_amount_fields = [
    'INVOICE_DATE: Confirm expense within tax year',
    'STATEMENT_DATE_RANGE: Validate bank statement coverage period',
    'IS_GST_INCLUDED: Determine GST credit eligibility',
    'GST_AMOUNT: Calculate claimable GST credits',
    'TOTAL_AMOUNT: Verify total expense claim amount'
]

# Card 3: Line Items with descriptions
line_item_fields = [
    'LINE_ITEM_DESCRIPTIONS: Assess work-related nature of each item',
    'LINE_ITEM_QUANTITIES: Validate reasonableness of purchases',
    'LINE_ITEM_PRICES: Check individual item costs',
    'LINE_ITEM_TOTAL_PRICES: Verify line-item calculations'
]

# Card 4: Transaction fields with descriptions
transaction_fields = [
    'TRANSACTION_DATES: Match payments to invoice dates',
    'TRANSACTION_AMOUNTS_PAID: Confirm actual payment amounts'
]

# Create wider cards to accommodate descriptions
create_clean_card(0.5, card_y, 4.8, card_height,
                 'General Document', 6,
                 general_fields,
                 colors['primary'], '📄')

create_clean_card(5.5, card_y, 4.8, card_height,
                 'Date & Amount', 5,
                 date_amount_fields,
                 colors['secondary'], '📅')

create_clean_card(10.5, card_y, 4.8, card_height,
                 'Line Items', 4,
                 line_item_fields,
                 colors['accent1'], '📋')

create_clean_card(15.5, card_y, 3.8, card_height,
                 'Transactions', 2,
                 transaction_fields,
                 colors['accent2'], '💳')

# Bottom summary bar with two lines of text
summary_rect = FancyBboxPatch((0.5, 0.2), 18.8, 1.2,
                              boxstyle="round,pad=0.02",
                              facecolor='#F8F9FA',
                              edgecolor=colors['dark'],
                              linewidth=1, linestyle='--', alpha=0.7)
ax.add_patch(summary_rect)

# Summary text with icons - larger
benefits_text = '✓ Automated Validation   ✓ Cross-Referencing   ✓ Compliance Checking   ✓ Audit Trail'
ax.text(10, 0.9, benefits_text, fontsize=13, ha='center', va='center',
        color=colors['dark'], fontweight='bold')

# Additional text at bottom - larger
ax.text(10, 0.4, 'Complete document capture ensures accurate expense substantiation',
        fontsize=12, ha='center', va='center',
        color=colors['text'], style='italic')

plt.tight_layout()
plt.savefig('/Users/tod/Desktop/ssd_du_presentation/17_fields_clean_cards.png',
            dpi=600, bbox_inches='tight', facecolor='none', transparent=True, pad_inches=0.1)
plt.close()

print("Clean cards infographic saved as '17_fields_clean_cards.png'")