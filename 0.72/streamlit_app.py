import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

import streamlit as st
from util.release_helper import create_static_notes

VERSION = '.'.join(st.__version__.split('.')[:2])

# Begin release updates
from demos.file_uploader import file_uploader

previous_version = "0.71.0"
demo_pages = {
    "Consolidate Re-runs for File Uploader": file_uploader
}

st.set_page_config(
    page_title=f"New features in Streamlit {VERSION}",
)

contributors = [
    "nicolaskruchten",
    "hendrik-teuber-by",
]

intro = """
This release focuses on continued cleanup and setting up a framework to enable
future work on theming. For more details, please check out our
[roadmap](https://github.com/streamlit/streamlit/wiki/Roadmap)
"""

release_notes = f"""
---
**Notable Changes**

- 🌈 Establish a framework for theming and migrate existing components.
- 📱 Improve the sidebar experience for mobile devices.
- 🧰 Consolidate re-runs for File Uploader 

"""
# End release updates

def draw_main_page():
    st.write(f"""
    # Welcome to Streamlit {VERSION}! 👋
    """)


    st.write(intro)

    st.write(release_notes)

    create_static_notes(contributors, previous_version, VERSION)


# Draw sidebar
pages = list(demo_pages.keys())

if len(pages):
    pages.insert(0, "Release Notes")
    st.sidebar.title(f"Streamlit v{VERSION} Demos")
    selected_demo = st.sidebar.radio("", pages)
else:
    selected_demo = "Release Notes"

# Draw main page
if selected_demo in demo_pages:
    demo_pages[selected_demo]()
else:
    draw_main_page()
