<template>
	<div class="nav_link">
		<a>Home</a>
		<a>Products</a>
		<a>About</a>
		<a>Contacts</a>
	</div>
</template>

<style lang="scss">
.nav_link {
	display: flex;
	align-items: center;
	color: rgba(255, 255, 255, 0.4);

	a {
		margin: 0 25px;
		transition: 0.3s;
		padding: 7px 15px;
		border-radius: 100px;
		background: rgba(209, 209, 209, 0.1);
		cursor: pointer;

		&:hover {
			transform: scale(110%);
			color: rgba(255, 255, 255, 0.8);
			border: 1.5px solid rgba(255, 255, 255, 0.161);
		}
		transition: 0.3s;
		border: 1.5px solid rgba(255, 255, 255, 0);
	}
}
</style>
