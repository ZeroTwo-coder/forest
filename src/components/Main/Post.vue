<template>
	<div v-for="post in posts" :key="post.id" class="post">
		<!-- <div
			class="image_post"
			:style="{ 'background-image': 'url({url})' }"
		></div> -->
		<div class="image_post">
			<img :src="require(`@/assets/${post.image}`)" alt="..." />
		</div>

		<div class="content_post">
			<h2>{{ post.title }}</h2>
			<p>
				{{ post.description }}
			</p>
			<a>Read More</a>
		</div>
	</div>
</template>
<script>
import axios from 'axios'
export default {
	data() {
		return {
			posts: null,
			ingurl: 'car.jpg',
		}
	},
	mounted() {
		axios
			.get('http://localhost:3000/post/')
			.then(response => (this.posts = response.data))
	},
}
</script>
<style lang="scss" scoped>
.post {
	display: flex;
	margin: 20px 0;
	background-color: rgba(255, 255, 255, 0.2);
	padding: 20px;
	width: 90%;
	border-radius: 70px;
	.image_post {
		// background-image: url('@/assets/car.jpg');
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
		overflow: hidden;

		img {
			width: 100%;
		}
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
