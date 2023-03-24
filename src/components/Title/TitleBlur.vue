<template>
	<div class="blur_title">
		<h1>WELCOME TO OUR WEBSITE</h1>
		<p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
	</div>
</template>
<style lang="scss" scoped>
.blur_title {
	background-color: rgba(68, 68, 68, 0.112);
	box-shadow: 0px 15px 30px rgba(97, 97, 97, 0.287);
	border-radius: 100px;
	border: 2px solid rgba(255, 255, 255, 0.3);
	backdrop-filter: blur(10px);
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	padding: 30px 90px;

	h1 {
		color: #ffffff;
		font-size: 80px;
		line-height: 0;
		margin-bottom: 50px;
	}
	p {
		color: white;
		font-size: 20px;
	}
}
</style>
