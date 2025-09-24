import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Set up the figure with transparent background - narrower to reduce margins
fig, ax = plt.subplots(figsize=(16, 7), facecolor='none')
ax.set_xlim(0, 16)
ax.set_ylim(0, 7)
ax.axis('off')

# Modern color palette
colors = {
    'primary': '#28A745',      # Green (new color for General Document)
    'secondary': '#FF6B35',    # Orange
    'accent1': '#00D9FF',      # Cyan
    'accent2': '#FFD93D',      # Yellow
    'dark': '#0066CC',         # Corporate blue (moved to header)
    'text': '#2C3E50',         # Dark gray
    'white': '#FFFFFF'
}

# Title section - centered with reduced margins
title_rect = FancyBboxPatch((0.5, 5.5), 15.0, 1.3,
                            boxstyle="round,pad=0.02",
                            facecolor=colors['dark'],
                            edgecolor='none')
ax.add_patch(title_rect)
ax.text(8, 6.4, '17 CRITICAL FIELDS', fontsize=28, fontweight='bold',
        color='white', ha='center', va='center')

# Subtitle inside the header box - white color
ax.text(8, 5.9, 'Work-Related Expense Substantiation Requirements',
        fontsize=16, color='white', ha='center', va='center')

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

    # Field list with bullets - proper spacing from header
    for i, field in enumerate(fields):
        # More space from header, much tighter between items to fit all fields
        y_pos = y + height - 0.85 - (i * 0.35)  # Reduced spacing to fit all 6 items
        # Bullet point closer to edge
        bullet = plt.Circle((x + 0.15, y_pos), 0.04,
                           facecolor=color, alpha=0.7)
        ax.add_patch(bullet)
        # Split field into name and description if colon present
        if ':' in field:
            field_name, field_desc = field.split(':', 1)
            # Field name in bold
            ax.text(x + 0.25, y_pos + 0.08, field_name + ':', fontsize=9,
                    color=colors['text'], va='top', ha='left', fontweight='bold')
            # Short description on single line
            ax.text(x + 0.25, y_pos - 0.08, field_desc.strip(), fontsize=8,
                    color=colors['text'], va='top', ha='left', alpha=0.85)
        else:
            # Field text without description
            ax.text(x + 0.25, y_pos, field, fontsize=10,
                    color=colors['text'], va='center', ha='left')

# Create the four cards with proper spacing
card_height = 3.2  # Shorter cards for concise text
card_y = 1.5  # Higher position

# Card 1: General Document with short descriptions
general_fields = [
    'DOCUMENT_TYPE: Classify document type',
    'BUSINESS_ABN: Verify legitimate ABN',
    'SUPPLIER_NAME: Identify supplier',
    'BUSINESS_ADDRESS: Confirm location',
    'PAYER_NAME: Match taxpayer records',
    'PAYER_ADDRESS: Verify address'
]

# Card 2: Date & Amount with short descriptions
date_amount_fields = [
    'INVOICE_DATE: Confirm tax year',
    'STATEMENT_DATE_RANGE: Validate period',
    'IS_GST_INCLUDED: Check GST eligibility',
    'GST_AMOUNT: Calculate GST credits',
    'TOTAL_AMOUNT: Verify claim amount'
]

# Card 3: Line Items with short descriptions
line_item_fields = [
    'LINE_ITEM_DESCRIPTIONS: Check work-related',
    'LINE_ITEM_QUANTITIES: Validate purchases',
    'LINE_ITEM_PRICES: Check item costs',
    'LINE_ITEM_TOTAL_PRICES: Verify calculations'
]

# Card 4: Transaction fields with short descriptions
transaction_fields = [
    'TRANSACTION_DATES: Match payments',
    'TRANSACTION_AMOUNTS_PAID: Confirm amounts'
]

# Create centered cards
create_clean_card(0.5, card_y, 3.6, card_height,
                 'General Document', 6,
                 general_fields,
                 colors['primary'], '📄')

create_clean_card(4.3, card_y, 3.6, card_height,
                 'Date & Amount', 5,
                 date_amount_fields,
                 colors['secondary'], '📅')

create_clean_card(8.1, card_y, 3.6, card_height,
                 'Line Items', 4,
                 line_item_fields,
                 colors['accent1'], '📋')

create_clean_card(11.9, card_y, 3.6, card_height,
                 'Transactions', 2,
                 transaction_fields,
                 colors['accent2'], '💳')

# Bottom summary bar with reduced margins
summary_rect = FancyBboxPatch((0.5, 0.2), 15.0, 1.2,
                              boxstyle="round,pad=0.02",
                              facecolor='#F8F9FA',
                              edgecolor=colors['dark'],
                              linewidth=1, linestyle='--', alpha=0.7)
ax.add_patch(summary_rect)

# Summary text with icons - larger
benefits_text = '✓ Automated Validation   ✓ Cross-Referencing   ✓ Compliance Checking   ✓ Audit Trail'
ax.text(8, 0.9, benefits_text, fontsize=13, ha='center', va='center',
        color=colors['dark'], fontweight='bold')

# Additional text at bottom - larger
ax.text(8, 0.4, 'Complete document capture ensures accurate expense substantiation',
        fontsize=12, ha='center', va='center',
        color=colors['text'], style='italic')

plt.tight_layout()
plt.savefig('/Users/tod/Desktop/ssd_du_presentation/17_fields_clean_cards.png',
            dpi=600, bbox_inches='tight', facecolor='none', transparent=True, pad_inches=0.1)
plt.close()

print("Clean cards infographic saved as '17_fields_clean_cards.png'")