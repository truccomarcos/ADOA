tmp="/tmp/mysql-tools.sh.tmp"

setup-db ( ) {
    cat <<EOF > $tmp
DROP DATABASE $adoa;
CREATE DATABASE $adoa;
GRANT USAGE on *.* to '${adoa}'@'localhost' IDENTIFIED BY '${adoa}';
GRANT ALL PRIVILEGES ON ${adoa}.* to '${adoa}'@'localhost';
EOF
    cat $tmp
    mysql -f -u ${root} -p${root} < $tmp
    rm $tmp
}
