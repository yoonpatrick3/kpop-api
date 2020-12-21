<html>

<title>Stumbl</title>

<link rel="stylesheet" type="text/css" href="style.css">

<body>

<div class="container">
<form action="input.php" method="post" class="form" autocomplete="off"><pre>
		First Name       <input type="text" name="fname">
		Music       	 <input type="text" name="music">
		Movie   	 <input type="text" name="movie">
		School		 <input type="text" name="school">
		Major		 <input type="text" name="major">
	        <input  type="submit" value="ADD RECORD">
	</pre></form>

</div>

</body>

<?php
    $url = 'C:/Users/12244/yoonp/independentCS/kpop/kpop_data.json'
    $data = file_get_contents($url); // put the contents of the file into a variable
    $json = json_decode($data); // decode the JSON feed

    echo '<pre>' . print_r($json, true) . '</pre>';
?>

</html>