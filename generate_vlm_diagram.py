#!/usr/bin/env python3
"""
Generate Vision-Language Model Architecture Diagram using Mermaid CLI.

This script creates a Mermaid diagram showing the VLM processing pipeline
with transparent data flow boxes and solid process boxes.
"""

import subprocess
from pathlib import Path


def create_mermaid_diagram():
    """Create Mermaid diagram code with transparent data flow boxes."""
    mermaid_code = """flowchart TD
    Input[WRE Document Image<br/>Raw pixel data]
    Input --> VisionEncoder[Vision Encoder<br/>InternViT or Llama]

    VisionEncoder --> VisualEmbed[Visual Embeddings<br/>Image patches]

    VisualEmbed --> Projector[Projector Layer<br/>MLP InternVL3<br/>Cross-attention Llama]

    ExtPrompt[Extraction Prompt<br/>Field instructions] --> TextToken[Text Tokenizer<br/>Token embeddings]

    Projector --> VisualTokens[Visual Tokens<br/>LLM-compatible]

    VisualTokens --> LLMDecoder[LLM Decoder<br/>Transformer]
    TextToken --> LLMDecoder

    LLMDecoder --> AttentionMech[Attention Mechanism<br/>Visual + Text fusion]

    AttentionMech --> TokenGen[Token Generation<br/>Sequential output]

    TokenGen --> StructuredOutput[Structured Extraction<br/>ABN: 12 345 678 901<br/>TOTAL: $137.50<br/>etc.]

    %% Styling
    classDef processBox fill:#ffcccc,stroke:#333,stroke-width:2px
    classDef dataFlow fill:transparent,stroke:transparent,color:#666
    classDef inputOutput fill:#ccffcc,stroke:#333,stroke-width:2px

    %% Apply styles
    class Input,StructuredOutput,ExtPrompt inputOutput
    class VisionEncoder,Projector,LLMDecoder,TokenGen processBox
    class VisualEmbed,TextToken,VisualTokens,AttentionMech dataFlow"""

    return mermaid_code


def main():
    """Generate VLM architecture diagram with transparent data flows."""
    # Create Mermaid diagram content
    diagram_content = create_mermaid_diagram()

    # Save to .mmd file
    mmd_file = Path("vlm_architecture_transparent.mmd")
    mmd_file.write_text(diagram_content)
    print(f"✅ Created Mermaid file: {mmd_file}")

    # Generate PNG using Mermaid CLI
    png_file = Path("vlm_architecture_transparent.png")

    try:
        # Run mmdc command to convert Mermaid to PNG with transparent background
        cmd = [
            "mmdc",
            "-i", str(mmd_file),
            "-o", str(png_file),
            "-b", "transparent",  # Transparent background
            "-w", "800",    # Width
            "-H", "1000"    # Height
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✅ Generated PNG diagram: {png_file}")
            print("📊 Diagram features:")
            print("   - Fully transparent data flow boxes (no borders)")
            print("   - Solid process boxes (Vision Encoder, LLM Decoder, etc.)")
            print("   - Clear input/output boxes in green")
            print("   - Transparent background")
        else:
            print(f"❌ Error generating PNG: {result.stderr}")

    except FileNotFoundError:
        print("❌ Mermaid CLI (mmdc) not found. Please install with: npm install -g @mermaid-js/mermaid-cli")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()