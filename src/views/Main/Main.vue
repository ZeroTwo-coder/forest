<template>
	<div class="main">
		<Post />
	</div>
</template>
<script>
import Post from '@/components/Main/Post.vue'
export default {
	components: {
		Post,
	},
}
</script>
<style lang="scss">
.main {
	width: 90%;
	margin: auto;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	border-radius: 30px;
	background-color: white;
	padding: 50px;
	box-shadow: 0 0 50px rgba(0, 0, 0, 0.4);
	background-color: rgba(143, 143, 143, 0.448);
	border-radius: 50px;
	backdrop-filter: blur(20px);
}
</style>
