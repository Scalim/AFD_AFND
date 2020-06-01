<template>
  <table>
    <tr>
      <th></th>
      <th :key="'c' + vertice" v-for="vertice in vertices">{{ vertice }}</th>
    </tr>

    <tr :key="'r' + vertice" v-for="(vertice, i) in vertices">
      <th>{{ vertice }}</th>
      <td :key="'e' + i + j" v-for="(elemento, j) in matriz[i]">
        {{ elemento }}
      </td>
    </tr>
  </table>
</template>

<style lang="scss">
table {
  text-align: center;

  td,
  th {
    padding: 5px 10px;
  }
}
</style>

<script>
export default {
  name: "Matriz",
  props: ["matriz", "vertices"],
  data: () => ({}),
};
</script>
