$(function() {
	try {
		var responseText = sendData("GET", "/parsing?path=" + path);
		var list = JSON.parse(responseText);
		var tbody = $("#table tbody");
		tbody.html("");

		for(i=0;i<list.length;i++) {
			var tr = "\
				<tr>\
				<td>" + (i+1) + "</td>\
				<td>" + (list[i].type) + " </td>\
				<td>" + (list[i].filename) + " </td>\
				<td>" + (list[i].size) + " </td>\
				<td>" + (list[i].path) + " </td>\
				<td>" + (list[i].mtime) + " </td>\
				<td>" + (list[i].atime) + " </td>\
				<td>" + (list[i].ctime) + " </td>\
				<td>" + (list[i].etime) + " </td>\
				</tr>\
			";
			tbody.append(tr);
		}
	}
	catch(exception){
		alert('input error!')
	}
});

function sendData(method, action, data="") {
	var wshttp = new XMLHttpRequest();
	wshttp.open(method, action, false);
	wshttp.setRequestHeader('Content-Type', 'application/x-www=form-urlencoded');
	wshttp.send(data);
	return wshttp.responseText;
}