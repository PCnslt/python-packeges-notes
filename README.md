# Create environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip
pip3 install pip --upgrade

# Install / run our package
pip3 install -e .

# After having a main function:
python3 -m shawn_r // Run through the main function.



# Build and upload to PiPy.org

`
pip3 install build
python3 -m build

pip3 install twine
python3 -m twine upload dist/* --skip`

# install packages
pip3 install tqdm

# MANIFEST.in = include files that are not python to be later included in the build artifacts. 
