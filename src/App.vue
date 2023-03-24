<template>
	<div class="wrapper">
		<div class="header">
			<Navigation />
			<Title />
		</div>
		<Main />
	</div>
</template>

<script>
import Navigation from '@/views/Header/Navigation.vue'
import Title from '@/views/Header/Title.vue'
import Main from '@/views/Main/Main.vue'
export default {
	components: {
		Navigation,
		Title,
		Main,
	},

	data() {
		return {}
	},
	methods: {},
	setup() {
		// const app = 2
		// console.log(app);
	},
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;400;500;700&display=swap');

* {
	padding: 0;
	margin: 0;
}

body {
	font-family: 'Ubuntu', sans-serif;
	background-image: url('@/assets/bg.jpg');
	background-size: cover;
	background-attachment: fixed;
	background-repeat: no-repeat;
	padding-bottom: 50px;
	.wrapper {
		width: 90%;
		margin: auto;
		.header {
			min-width: 100%;
			height: 100vh;
		}
	}
}
</style>
