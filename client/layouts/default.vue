<template>
    <div>
        <DefaultHeader />
        <slot />
    </div>
</template>

<script>
import DefaultFooter from "./DefaultFooter.vue";
import DefaultHeader from "./DefaultHeader.vue";

export default {
    data() {
        return {

        };
    },
    components: { DefaultFooter, DefaultHeader }
}

</script>
