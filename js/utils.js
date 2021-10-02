function getRandomId(tipe = 'string', length = 5, between = null) {

    if (tipe == 'number' && between)
        return Math.random().toString(between).substr(2, length);
    else
        return Math.random().toString(20).substr(2, length)
}

/**
 * 
 * @param {String} time 
 * @param {String} format 
 * @returns Date
 */
function getTime(time = null, format = 'mysql_timestamp') {        
    if (format == 'mysqltimestamp')
        format = 'YYYY-MM-DD HH:mm:ss';
    if (!time)
        time = new Date();

    return moment(time).format(format);
}