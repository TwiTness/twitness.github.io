<?php
/**
 * http.test.py server file
 */
class _A {
	public $a, $b, $c;
}

class _B {
	public $x, $y, $z;
}

class MD {

	public function md() {
		$_a = new _A();
		$_b = new _B();

		$_a->a = self::getParams($_GET, 'a', '');
		$_a->b = self::getParams($_GET, 'b', '');
		$_a->c = self::getParams($_GET, 'c', '');
		$_b->x = self::getParams($_POST, 'x', '');
		$_b->y = self::getParams($_POST, 'y', '');
		$_b->z = self::getParams($_POST, 'z', '');


		$obj = array();
		$obj['a'] = $_a;
		$obj['b'] = $_b;
		$s = array();
		foreach ($_SERVER as $key => $server) {
			if(strpos($key, 'HTTP_') !== FALSE) $s[$key] = $server;
		}
		$obj['server'] = $s;
		return $obj;
	}


	public static function getParams($arr, $key, $default = '') {
		return isset($arr[$key]) ? $arr[$key] : $default;
	}


}

$md = new MD();
$response = $md->md();
if (isset($_GET['st']) && $_GET['st']) {
	print_r($response);
} else {
	echo json_encode($response) . "\n";

}
?>