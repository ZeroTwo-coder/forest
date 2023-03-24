<template>
	<div class="nav">
		<Logo />
		<Menu />
	</div>
</template>

<script>
import Logo from '../../components/Navigation/Logo.vue'
import Menu from '../../components/Navigation/Menu.vue'
export default {
	components: {
		Logo,
		Menu,
	},
}
</script>

<style lang="scss" scoped>
.nav {
	&:hover {
		border: 3px solid rgba(255, 255, 255, 0.161);
	}
	transition: 0.3s;
	border: 3px solid rgba(255, 255, 255, 0);
	position: fixed;
	width: 85%;
	display: flex;
	justify-content: space-between;
	margin-top: 20px;
	padding: 7px 40px;
	background-color: rgba(255, 255, 255, 0.1);
	border-radius: 100px;
	backdrop-filter: blur(10px);
	z-index: 10;
}
</style>
