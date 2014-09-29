<?php
/**
 * http.test.py server file
 */
if(!isset($_POST['user'])) {
	Header("WWW-Authenticate: Basic realm=\"SSS\"");
	Header("HTTP/1.0 401 Unauthorized");
	echo "Text to send if user hits Cancel buttonn";
	exit;
} else {
	if ( !($_POST['user']=="user" && $_POST['passwd']=="passwd") ) {
		// 错误用户名称/密码强制再验证
		Header("WWW-Authenticate: Basic realm=\"SSS\"");
		Header("HTTP/1.0 401 Unauthorized");
		echo "ERROR : " . $_POST['user'] . "/" . $_POST['passwd'] ." is invalid.";
		exit(0);
	} else {
		echo "Welcome user!";
	}
}
?>