<template>
	<div class="btn_create">
		<a>Create Post</a>
	</div>
</template>
<style lang="scss">
.btn_create {
	background-color: rgba(68, 68, 68, 0.112);
	border-radius: 100px;
	backdrop-filter: blur(8px);
	color: white;
	padding: 20px 40px;
	margin-top: 70px;
	font-size: 18px;
	cursor: pointer;
	transition: 0.3s;
	border: 2px solid rgba(255, 255, 255, 0.216);

	&:hover {
		transform: scale(110%);
	}
}
</style>
