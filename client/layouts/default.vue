<template>
    <div>
        <DefaultHeader />
        <div class=" pt-28 px-32">
        <slot />
        </div>
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
