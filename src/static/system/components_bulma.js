Vue.component("select-boolean", {
  template: `
    <el-select @change="change" v-model="value"
      placeholder="Seleccione un valor">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
  `,
  data(){
    return {
      loading: false,
      options: [
        {label: 'positivo', value: 1},
        {label: 'negativo', value: 0},
      ],
      value: ''
    }
  },
  methods: {
    change(value){
      this.$emit("change", value)
      this.$emit("input", value)
    }
  },
})

Vue.component("select-usuario", {
  template: `
    <el-select @change="change" v-model="value"
      filterable
      clearable
      remote
      reserve-keyword
      placeholder="Seleccione un Usuario"
      :remote-method="remoteMethod"
      :loading="loading">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
  `,
  data(){
    return {
      loading: false,
      options: [],
      value: ''
    }
  },
  methods: {
    change(value){
      this.$emit("change", value)
    },
    remoteMethod(query){
      _axios({
        url: '/users/finder/',
        method: 'get',
        params: {
          kw: query
        }
      }).then(rsp => {
        this.options = rsp.data.usuarios
      })
    }
  },
  mounted(){
    this.remoteMethod()
  }
})

Vue.component("select-analisis", {
  template: `
    <el-select @change="change" v-model="value"
      filterable
      clearable
      remote
      reserve-keyword
      placeholder="Seleccione un analisis"
      :remote-method="remoteMethod"
      :loading="loading">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item">
      </el-option>
    </el-select>
  `,
  data(){
    return {
      loading: false,
      options: [],
      value: ''
    }
  },
  methods: {
    change(value){
      this.$emit("change", value)
      this.$emit("input", value)
    },
    remoteMethod(query){
      _axios({
        url: '/analisis/',
        method: 'post',
        params: {
          kw: query
        }
      }).then(rsp => {
        this.options = rsp.data.results
      })
    }
  },
  mounted(){
    this.remoteMethod()
  }
})

Vue.component("combo-usuario", {
    template: `
      <div class="field">
        <label class="label">Usuario</label>
        <div class="control has-icons-left has-icons-right">
          <select-usuario @change="change"></select-usuario>
        </div>
      </div>
    `,
    methods: {
      change(value){
        this.$emit('input', value)
      }
    }
})

Vue.component("combo-analisis", {
  template: `
    <div class="field">
      <label class="label">Analisis</label>
      <div class="control has-icons-left has-icons-right">
        <select-analisis @change="change"></select-analisis>
      </div>
    </div>
  `,
  methods: {
    change(value){
      this.$emit('input', value)
    }
  }
})

Vue.component("controlador", {
    props: {
      label: {
        type: String,
        default: ''
      }
    },
    template: `
      <div class="field">
        <label class="label" v-text="label"></label>
        <div class="control has-icons-left has-icons-right">
          <slot></slot>
        </div>
      </div>
    `
})