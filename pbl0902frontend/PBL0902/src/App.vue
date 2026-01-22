<template>
  <div class="app">
    <h1>Cars CRUD (FastAPI Multiverse)</h1>

    <!-- Backend switcher -->
    <label>
      Backend:
      <select v-model="selectedPort">
        <option value="4001">localhost:4001</option>
        <option value="4002">localhost:4002</option>
        <option value="4003">localhost:4003</option>
      </select>
    </label>

    <p class="info">
      Active API: {{ baseUrl }}
    </p>

    <hr />

    <!-- Fetch -->
    <button @click="fetchCars">Fetch Cars</button>

    <!-- Create -->
    <h3>Create Car</h3>
    <input v-model="form.carname" placeholder="Name" />
    <input v-model="form.carbrand" placeholder="Brand" />
    <input v-model="form.carmodel" placeholder="Model" />
    <input v-model.number="form.carprice" placeholder="Price" />
    <button @click="createCar">Create</button>

    <!-- Delete -->
    <h3>Delete Car</h3>
    <input v-model.number="deleteId" placeholder="Car ID" />
    <button @click="deleteCar">Delete</button>

    <!-- Results -->
    <h3>Result</h3>
    <pre>{{ result }}</pre>
  </div>
</template>

<script setup>
import { ref, computed } from "vue"

const selectedPort = ref("4001")

const baseUrl = computed(() => {
  return `http://localhost:${selectedPort.value}`
})

const result = ref(null)

const form = ref({
  carname: "",
  carbrand: "",
  carmodel: "",
  carprice: 0,
})

const deleteId = ref(null)

/* ---------- API helpers ---------- */

async function api(path, payload = {}) {
  const res = await fetch(`${baseUrl.value}${path}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  })

  if (!res.ok) {
    const err = await res.json()
    throw err
  }

  return res.json()
}

/* ---------- Actions ---------- */

async function fetchCars() {
  try {
    result.value = await api("/cars/fetch")
  } catch (e) {
    result.value = e
  }
}

async function createCar() {
  try {
    result.value = await api("/cars/create", form.value)
  } catch (e) {
    result.value = e
  }
}

async function deleteCar() {
  try {
    result.value = await api("/cars/delete", {
      id: deleteId.value,
    })
  } catch (e) {
    result.value = e
  }
}
</script>

<style scoped>
.app {
  font-family: sans-serif;
  padding: 20px;
  max-width: 600px;
}

input,
select {
  display: block;
  margin: 6px 0;
  padding: 4px;
}

button {
  margin-top: 6px;
}

.info {
  font-size: 0.9em;
  color: #666;
}
</style>
