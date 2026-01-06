import matplotlib.pyplot as plt

def draw_instruction_format(title, fields, sizes):
    """
    Draws a simple instruction format diagram.
    title: str, name of the instruction type
    fields: list of field names (e.g., ["Opcode", "Operand"])
    sizes: list of relative sizes for each field (e.g., [1, 2])
    """
    fig, ax = plt.subplots(figsize=(6, 1))
    total_size = sum(sizes)
    start = 0

    for field, size in zip(fields, sizes):
        ax.add_patch(plt.Rectangle((start/total_size, 0), size/total_size, 1, 
                                   edgecolor="black", facecolor="lightgrey"))
        ax.text(start/total_size + (size/total_size)/2, 0.5, field, 
                ha="center", va="center", fontsize=10, weight="bold")
        start += size

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    plt.title(title, fontsize=12, weight="bold")
    return fig

# Draw three instruction formats
fig1 = draw_instruction_format("Zero-Address Instruction Format", ["Opcode"], [3])
fig2 = draw_instruction_format("One-Address Instruction Format", ["Opcode", "Operand"], [1, 2])
fig3 = draw_instruction_format("Two-Address Instruction Format", ["Opcode", "Operand1", "Operand2"], [1, 1, 1])

plt.show()
