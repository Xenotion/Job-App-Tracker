<template>
    <div id="main-layout">
      <!-- Global Header or Navbar -->
      <header v-if="!$route.meta.hideLayout">

      </header>
  
      <!-- Dynamic content rendered based on the route -->
      <main>
        <router-view />
        
      </main>
  
      <!-- Global Footer -->
      <footer v-if="!$route.meta.hideLayout">
        <nav>
          <router-link to="/jobs">Jobs</router-link>
        </nav>
        <p>© 2023 My Vue App</p>
      </footer>
    </div>
</template>

<style>
/* Your styles here */
</style>
