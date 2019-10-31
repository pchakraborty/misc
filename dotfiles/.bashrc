for rcfile in $(ls -I exclude -I "*~" $HOME/.bashrc.d); do
    if [ ! -d "$rcfile" ]; then
        source $HOME/.bashrc.d/$rcfile
    fi
done
