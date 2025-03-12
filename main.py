import streamlit as st
import sys
from pathlib import Path
from src.entry import entry_point
from src.logger import logger

def entry_point_for_args(args):
    if args["debug"] is True:
        # Disable tracebacks
        sys.tracebacklimit = 0
    for root in args["input_paths"]:
        entry_point(
            Path(root),
            args,
        )

def main():
    st.title("OMRChecker UI")

    # Input directory
    input_paths = st.text_area(
        "Input Directory(s)",
        value="inputs",
        help="Enter the input directory or files (comma separated)."
    )
    input_paths = input_paths.split(',')

    # Output directory
    output_dir = st.text_input(
        "Output Directory",
        value="outputs",
        help="Specify the output directory."
    )

    # Debug option
    debug = st.checkbox("Enable Debug Mode", value=False, help="Enable debugging for detailed errors.")

    # Auto Align option
    auto_align = st.checkbox(
        "Enable Auto Alignment (Experimental)",
        value=False,
        help="Enables automatic template alignment if scans are misaligned."
    )

    # Set Layout option
    set_layout = st.checkbox(
        "Set Layout for OMR Template",
        value=False,
        help="Set up the OMR template layout and modify the JSON file."
    )

    # Run button to execute the logic
    if st.button("Run OMR Checker"):
        # Prepare arguments for the script
        args = {
            "input_paths": input_paths,
            "debug": debug,
            "output_dir": output_dir,
            "autoAlign": auto_align,
            "setLayout": set_layout
        }
        
        # Call the entry point function
        entry_point_for_args(args)

        st.success("OMR processing completed successfully.")

if __name__ == "__main__":
    main()
