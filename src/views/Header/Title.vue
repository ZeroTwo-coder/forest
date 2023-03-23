<template>
	<div class="title">
		<TitleBlur />
		<TitleBtn />
	</div>
</template>
<script>
import TitleBlur from '@/components/Title/TitleBlur.vue'
import TitleBtn from '@/components/Title/TitleBtn.vue'
export default {
	components: {
		TitleBlur,
		TitleBtn,
	},
}
</script>
<style lang="scss">
.title {
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	height: 100%;
}
</style>
