<template>
  <section>
    <section class="hero is-primary is-fullheight is-bold has-text-centered">
      <div class="hero-body">
        <div class="container">
          <p class="logo">
            <img src="/static/Logomakr_1zxkZd.png" />
          </p>
          <h2 class="subtitle">
            Welcome to ICW, a forum to try out AI colorization engine.
          </h2>
          <a class="button is-medium is-primary is-inverted" @click="showAuthModal = true">
            Login and Join Us
          </a>
        </div>
      </div>
    </section>
    <section>
      <b-modal :active.sync="showAuthModal">
        <div class="modal-card has-text-centered">
          <b-tabs v-model="activeTab">
            <b-tab-item label="Login">
              <section class="modal-card-body">
                <b-field>
                  <b-input placeholder="Username" v-model="username" required></b-input>
                </b-field>
                <b-field>
                  <b-input type="password" placeholder="Password" v-model="password" required></b-input>
                </b-field>
              </section>
              <footer class="modal-card-foot">
                <button class="button is-primary is-fullwidth" @click="tryLogin">Login</button>
              </footer>
            </b-tab-item>

            <b-tab-item label="Register">
              <section class="modal-card-body">
                <b-field>
                  <b-input placeholder="Display Name" v-model="displayName" required></b-input>
                </b-field>
                <b-field>
                  <b-input placeholder="Username" v-model="username" required></b-input>
                </b-field>
                <b-field>
                  <b-input type="password" password-reveal placeholder="Password" v-model="password" required></b-input>
                </b-field>
              </section>
              <footer class="modal-card-foot">
                <button class="button is-primary is-fullwidth" @click="tryRegister">Register</button>
              </footer>
            </b-tab-item>
          </b-tabs>
        </div>
      </b-modal>
    </section>
  </section>
</template>

<script>
export default {
  data () {
    return {
      showAuthModal: false,
      activeTab: 0,
      username: '',
      password: '',
      displayName: ''
    }
  },
  methods: {
    async tryLogin () {
      try {
        await this.$store.dispatch('auth/login', {
          'username': this.username,
          'password': this.password
        })
        location.replace('/dashboard')
      } catch (err) {
        this.errorMsg('Failed to login. Check for network, username and password.')
      }
    },
    async tryRegister () {
      try {
        await this.$store.dispatch('auth/register', {
          'username': this.username,
          'password': this.password,
          'display_name': this.displayName
        })
        location.replace('/dashboard')
      } catch (err) {
        this.errorMsg('Failed to register. Network failure or username is already used.')
      }
    }
  }
}
</script>

<style scoped lang="scss">
.logo img {
  height: 5em;
  margin-bottom: 3em;
}

.b-tabs {
  background-color: white;
  border-radius: 4px;

  /deep/ .tabs {
    line-height: 2.5;
  }
}
</style>
