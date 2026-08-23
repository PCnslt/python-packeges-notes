from pathlib import Path
from .speakers import Shawn

def main():
    Shawn().print_name()
    
    with (Path(__file__).parent / "names.txt").open as f:
        f.read()
    
    
if __name__=="__main__":
    main()