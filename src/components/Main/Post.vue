<template>
	<div class="post">
		<!-- <div
			class="image_post"
			:style="{ 'background-image': 'url({url})' }"
		></div> -->
		<div class="image_post"></div>
		<div class="content_post">
			<h2>Lorem ipsum dolor sit.</h2>
			<p>
				Lorem ipsum dolor, sit amet consectetur adipisicing elit. Facilis
				blanditiis, voluptatibus officia reprehenderit est ipsam?
			</p>
			<a>Read More</a>
		</div>
	</div>
</template>
<style lang="scss">
.post {
	display: flex;
	margin: 20px 0;
	background-color: rgba(255, 255, 255, 0.2);
	padding: 20px;
	width: 90%;
	border-radius: 70px;
	.image_post {
		background-image: url('@/assets/girl.jpg');
		background-size: cover;
		background-repeat: no-repeat;
		width: 350px;
		height: 200px;
		border-radius: 50px;
		transition: 0.3s;
		// &:hover {
		// 	width: 250px;
		// 	height: 250px;
		// }
	}

	.content_post {
		display: flex;
		flex-direction: column;
		// align-items: center;
		justify-content: center;
		margin-left: 20px;
		color: white;

		h2 {
			font-size: 30px;
		}

		p {
			margin-top: 5px;
			width: 80%;
		}

		a {
			background-color: #ffffff1d;
			width: 150px;
			text-align: center;
			padding: 10px;
			border-radius: 100px;
			backdrop-filter: blur(3px);
			color: white;
			margin-top: 20px;
		}
	}
}
</style>
