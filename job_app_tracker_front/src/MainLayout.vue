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
        <p>© 2023 Xenotion</p>
      </footer>
    </div>
</template>

<style>
/* Basic styling for the <nav> */
  nav {
    background-color: #333;  /* Dark background */
    padding: 1em;
    text-align: center;  /* Center the links */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Shadow for depth */
    width: 5%;
    margin: auto;
    transition: background-color 0.3s;  /* Smooth transition for hover effect */

}

/* Styling for the router-link which is rendered as an anchor tag */
nav a {
    color: #ffffff;  /* White text */
    text-decoration: none;  /* Remove underline */
    padding: 0.5em 1em;  /* Padding around the link for better clickability */
    border-radius: 4px;  /* Rounded corners for the link */
}

/* Hover effect */
nav:hover {
    background-color: #555;  /* Slightly lighter shade on hover */
    color: #fff;  /* Keeping the text color white on hover */
}

</style>
