clear
sudo chmod +x uninstall

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/usociety"
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true

    pkg install -y git python2
elif [ "$(uname)" = "Darwin" ]; then
    INSTALL_DIR="/usr/local/usociety"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false
else
    INSTALL_DIR="$HOME/.usociety"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false

    sudo apt-get install -y git python3
fi

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[◉] A directory fsociety was found! Do you want to replace it? [Y/n]:" ;
    read mama
    if [ "$mama" = "y" ]; then
        if [ "$TERMUX" = true ]; then
            rm -rf "$INSTALL_DIR"
            rm "$BIN_DIR/usociety*"
        else
            sudo rm -rf "$INSTALL_DIR"
            sudo rm "$BIN_DIR/usociety*"
        fi
    else
        echo "[✘] If you want to install you must remove previous installations [✘] ";
        echo "[✘] Installation failed! [✘] ";
        exit
    fi
fi
echo "[✔] Cleaning up old directories...";
if [ -d "$ETC_DIR/Umer" ]; then
    echo "$DIR_FOUND_TEXT"
    if [ "$TERMUX" = true ]; then
        rm -rf "$ETC_DIR/Umer"
    else
        sudo rm -rf "$ETC_DIR/Umer"
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone --depth=1 https://github.com/MrRobot-hub/usociety "$INSTALL_DIR";
echo "#!$BASH_PATH
python $INSTALL_DIR/usociety.py" '${1+"$@"}' > "$INSTALL_DIR/usociety";
chmod +x "$INSTALL_DIR/usociety";
if [ "$TERMUX" = true ]; then
    cp "$INSTALL_DIR/usociety" "$BIN_DIR"
    cp "$INSTALL_DIR/usociety.cfg" "$BIN_DIR"
else
    sudo cp "$INSTALL_DIR/usociety" "$BIN_DIR"
    sudo cp "$INSTALL_DIR/usociety.cfg" "$BIN_DIR"
fi
rm "$INSTALL_DIR/usociety";


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
    echo "[✔] Tool installed successfully! [✔]";
    echo "";
    echo "[✔]====================================================================[✔]";
    echo "[✔]      All is done!! You can execute tool by typing usociety !       [✔]";
    echo "[✔]====================================================================[✔]";
    echo "";
else
    echo "[✘] Installation failed! [✘] ";
    exit
fi
