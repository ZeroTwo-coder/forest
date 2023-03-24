<template>
	<div
		:on-scroll="abc"
		v-show="active"
		v-for="post in posts"
		:key="post.id"
		class="post"
	>
		<!-- <div class="image_post">
			<img :src="require(`@/assets/${post.image}`)" alt="..." />
		</div> -->
		<div class="block_image">
			<img :src="require(`@/assets/${post.image}`)" alt="" />
		</div>
		<div class="content">
			<h1>{{ post.title }}</h1>
			<p>{{ post.description }}</p>
		</div>
		<button class="hide" @click="delete_post(post.id)">Hide</button>
	</div>
</template>
<script>
import axios from 'axios'
export default {
	data() {
		return {
			posts: null,
			active: true,
		}
	},
	mounted() {
		axios
			.get('http://localhost:3000/post/')
			.then(response => (this.posts = response.data))
	},

	methods: {
		delete_post(self, id) {
			axios.delete(`http://localhost:3000/post/${id}`).then(response => {
				console.log(response)
			})
		},
	},
}
</script>
<style lang="scss" scoped>
.post {
	display: flex;
	justify-content: space-between;
	color: white;
	margin: 20px 0;
	background: rgb(136, 136, 136);
	background: radial-gradient(
		circle,
		rgba(115, 115, 115, 0.168) 0%,
		rgba(255, 255, 255, 0.173) 100%
	);
	border: solid 0px #ffffff43;
	transition: 0.3s;
	&:hover {
		border: solid 2px #ffffff43;
		transform: scale(105%);
	}
	padding: 20px;
	width: 90%;
	border-radius: 50px;

	.block_image {
		width: 300px;
		overflow: hidden;
		border-radius: 30px;

		img {
			width: 100%;
		}
	}

	.hide {
		align-self: center;
		width: 100px;
		height: 40px;
		border-radius: 20px;
		color: #fcfcfc;
		background-color: rgba(194, 37, 37, 0.472);
		border: none;
		transition: 0.3s ease;
		cursor: pointer;
		&:hover {
			transform: scale(110%);
			background-color: rgba(194, 37, 37, 0.611);
		}
	}
	.content {
		h1 {
			font-size: 35px;
		}

		p {
			width: 600px;
		}
	}
}
</style>
