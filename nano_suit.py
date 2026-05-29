import numpy as np
import colorsys
import random
import plotly.graph_objects as go

from plotly.subplots import make_subplots

from PIL import Image

from ase import Atoms, Atom
from ase.visualize import view
from ase.io import write

# -----------------------------------
# LOAD IMAGE
# -----------------------------------
# IMAGE_PATH = "ironMan.png"
def plot_nanotech_heatmaps(IMAGE_PATH):


    img = Image.open(IMAGE_PATH).convert("L")

    img = img.resize((140, 140))

    pixels = np.array(img)

    # Fix orientation
    pixels = np.flipud(pixels)

    # -----------------------------------
    # CREATE STRUCTURE
    # -----------------------------------

    ase_atoms = Atoms()

    threshold = 150

    xy_scale = 0.45
    z_scale = 14

    # -----------------------------------
    # VISUAL EFFECT STORAGE
    # -----------------------------------

    custom_colors = []

    # -----------------------------------
    # HEATMAP STORAGE
    # -----------------------------------

    generated_heatmap = np.zeros_like(
        pixels,
        dtype=np.float32
    )

    # -----------------------------------
    # BUILD NANO PARTICLES
    # -----------------------------------

    for y in range(pixels.shape[0]):

        for x in range(pixels.shape[1]):

            brightness = pixels[y, x]

            # Dark regions become nanotech
            if brightness < threshold:

                xpos = x * xy_scale
                ypos = y * xy_scale

                # -----------------------------------
                # DIAMOND-LIKE SURFACE DEPTH
                # -----------------------------------

                zpos = (
                    ((255 - brightness) / 255) * z_scale
                    + random.uniform(0, 2)
                )

                # -----------------------------------
                # MATERIAL ASSIGNMENT
                # -----------------------------------

                # Gold regions
                if brightness < 45:

                    element = "Au"

                    h = 0.12
                    s = 0.65

                    # Diamond shine
                    v = 0.85 + random.uniform(0, 0.15)

                # Red armor
                else:

                    element = "Fe"

                    h = random.uniform(0.97, 1.0)

                    s = 0.82

                    # Reflective metallic shine
                    v = 0.45 + random.uniform(0, 0.45)

                # -----------------------------------
                # RANDOM DIAMOND SPARKLES
                # -----------------------------------

                sparkle = random.random()

                if sparkle > 0.985:

                    # Diamond nanoparticle
                    element = "C"

                    # Bright crystal white-blue
                    h = random.uniform(0.5, 0.65)

                    s = random.uniform(0.05, 0.25)

                    v = 1.0

                    # Elevated sparkle
                    zpos += random.uniform(2, 5)

                # -----------------------------------
                # ARC REACTOR GLOW
                # -----------------------------------

                center_x = pixels.shape[1] / 2
                center_y = pixels.shape[0] / 2

                dist = np.sqrt(
                    (x - center_x)**2 +
                    (y - center_y)**2
                )

                if dist < 10:

                    element = "Ag"

                    h = 0.55
                    s = 0.35
                    v = 1.0

                    zpos += 2

                # -----------------------------------
                # HSV -> RGB
                # -----------------------------------

                rgb = colorsys.hsv_to_rgb(h, s, v)

                custom_colors.append(rgb)

                # -----------------------------------
                # STORE GENERATED HEATMAP VALUE
                # -----------------------------------

                generated_heatmap[y, x] = zpos

                # -----------------------------------
                # ADD PARTICLE
                # -----------------------------------

                ase_atoms.append(
                    Atom(
                        element,
                        (xpos, ypos, zpos)
                    )
                )

    # -----------------------------------
    # NORMALIZE GENERATED HEATMAP
    # -----------------------------------

    generated_heatmap = (
        generated_heatmap /
        generated_heatmap.max()
    ) * 255

    generated_heatmap = generated_heatmap.astype(np.uint8)

    # -----------------------------------
    # ALPHA BLENDING
    # -----------------------------------

    alpha = 0.6

    blended_heatmap = (
        alpha * pixels +
        (1 - alpha) * generated_heatmap
    )

    blended_heatmap = blended_heatmap.astype(np.uint8)

    # -----------------------------------
    # ROTATE IMAGES
    # -----------------------------------

    # 180 degree rotation

    pixels = np.rot90(
        pixels,
        k=-1
    )

    pixels = np.rot90(
        pixels,
        k=-1
    )

    generated_heatmap = np.rot90(
        generated_heatmap,
        k=-1
    )

    generated_heatmap = np.rot90(
        generated_heatmap,
        k=-1
    )

    generated_heatmap = np.rot90(
        generated_heatmap,
        k=-1
    )

    blended_heatmap = np.rot90(
        blended_heatmap,
        k=-1
    )

    blended_heatmap = np.rot90(
        blended_heatmap,
        k=-1
    )
    blended_heatmap = np.rot90(
        blended_heatmap,
        k=-1
    )

    blended_heatmap = np.rot90(
        blended_heatmap,
        k=-1
    )

    # -----------------------------------
    # DISPLAY HEATMAPS WITH PLOTLY
    # -----------------------------------

    fig = make_subplots(
        rows=1,
        cols=3,
        subplot_titles=(
            "Nano Heatmap",
            "Rotated Original Heatmap",
            "Original Heatmap",
           
        )
    )

    # -----------------------------------
    # ORIGINAL HEATMAP
    # -----------------------------------

    fig.add_trace(

        go.Heatmap(
            z=blended_heatmap,
            colorscale='Inferno',
            showscale=False
        ),

        row=1,
        col=1
    )

    # -----------------------------------
    # GENERATED NANO HEATMAP
    # -----------------------------------

    fig.add_trace(

        go.Heatmap(
            z=generated_heatmap,
            colorscale='Plasma',
            showscale=False
        ),

        row=1,
        col=2
    )

    # -----------------------------------
    # BLENDED HEATMAP
    # -----------------------------------

    fig.add_trace(

        go.Heatmap(
            z=pixels,
            colorscale='Magma',
            showscale=True
        ),

        row=1,
        col=3
    )

    # -----------------------------------
    # LAYOUT
    # -----------------------------------

    fig.update_layout(

        title="Iron Man Nanotech Heatmaps",

        height=600,
        width=1500,

        template="plotly_dark"
    )

    # Remove axis ticks
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)

    return fig
    
def plot_fig(fig):
    fig.show()
    

if __name__ == "__main__":
    image_path = r"C:\Users\prakhar.a.gandhi\Downloads\Accenture\nano_tech\ironMan.png"
    fig = plot_nanotech_heatmaps(image_path)
    plot_fig(fig)