<!-- eslint-disable -->

<template>
    <h1>Job Application Tracker</h1>
    <button class="addjob_button" @click="addJob()">Add Job</button><br>
    <input class="searchbar" type="text" v-model="searchTerm" placeholder="Search for a company..." />

    <div class="jobs_container">
    <table>
      <thead>
        <tr>
            <th @click="sortTable('company_name')">Company</th>
            <th @click="sortTable('role_position')">Role</th>
            <th @click="sortTable('initial_application_submission_date')">Application Date</th>
            <th @click="sortTable('Round 1')">Round 1</th> 
            <th @click="sortTable('Round 2')">Round 2</th> 
            <th @click="sortTable('Round 3')">Round 3</th> 
            <th @click="sortTable('result')">Result</th>
            <th>Edit</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="job in filteredJobs" :key="job.id">
            <td>{{ job.company_name }}</td>
            <td>{{ job.role_position }}</td>
            <td>{{ job.initial_application_submission_date }}</td>

            <td v-if="job.application_type === 'A'">
                {{ job.type_a.online_assessment_date }}
                <span :class="job.type_a.online_assessment_completed ? 'check' : 'cross'">
                    {{ job.type_a.online_assessment_completed ? '✔️' : '❌' }}
                </span>
            </td>
            <td v-if="job.application_type === 'A'">
                {{ job.type_a.digital_interview_date }}
                <span :class="job.type_a.digital_interview_completed ? 'check' : 'cross'">
                    {{ job.type_a.digital_interview_completed ? '✔️' : '❌' }}
                </span>
            </td>
            <td v-if="job.application_type === 'A'">
                {{ job.type_a.assessment_centre_date }}
                <span :class="job.type_a.assessment_centre_completed ? 'check' : 'cross'">
                    {{ job.type_a.assessment_centre_completed ? '✔️' : '❌' }}
                </span>
            </td>

            <td v-if="job.application_type === 'B'">
                {{ job.type_b.recruiter_interview_date}}
                <span :class="job.type_b.recruiter_interview_completed ? 'check' : 'cross'">
                    {{ job.type_b.recruiter_interview_completed ? '✔️' : '❌' }}
                </span>
            </td>
            <td v-if="job.application_type === 'B'">
                {{ job.type_b.technical_interview_date }}
                <span :class="job.type_b.digital_interview_completed ? 'check' : 'cross'">
                    {{ job.type_b.digital_interview_completed ? '✔️' : '❌' }}
                </span>
            </td>
            <td v-if="job.application_type === 'B'">
                {{ job.type_b.behavioural_interview_date }}
                <span :class="job.type_b.behavioural_interview_completed ? 'check' : 'cross'">
                    {{ job.type_b.behavioural_interview_completed ? '✔️' : '❌' }}
                </span>
            </td>

            <td :class="getResultClass(job.result)">{{ job.result }}</td>
            <td>
                <div class="buttons-container">
                <button @click="editJob(job)">Update</button>
                <button @click="deleteJob(job)">Delete</button>
                </div>
            </td>
        </tr>
      </tbody>
    </table>
  </div>

    <div v-if="showForm" class="add_job">
        <form v-on:submit.prevent="submitForm">
            <div class="form-content">
                <div class="form-group">
                    <label for="company_name">Company Name</label>
                    <input type="text" class="form-control" id="company_name" v-model="company_name">
                </div>
                <div class="form-group">
                    <label for="role_position">Role/Position</label>
                    <input type="text" class="form-control" id="role_position" v-model="role_position">
                </div>
                <div class="form-group">
                    <label for="initial_application_submission_date">Submission Date</label>
                    <input type="date" class="form-control" id="initial_application_submission_date" v-model="initial_application_submission_date">
                </div>
                <div class="form-group">
                    <label for="application_type">Application Type</label>
                    <select id="application_type" v-model="application_type">
                        <option value="A">Type A Process</option>
                        <option value="B">Type B Process</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="result">Result</label>
                    <select id="result" v-model="result">
                        <option value="Waiting">Waiting</option>
                        <option value="Offer">Offer</option>
                        <option value="Rejected">Rejected</option>
                    </select>
                </div>
                <div v-if="application_type === 'A'">
                    <div class="form-group">
                        <label for="online_assessment_date">Online Assessment Date</label>
                        <input type="date" class="form-control" id="online_assessment_date" v-model="type_a.online_assessment_date">
                        <div class="input-container-2">
                            <label for="online_assessment_completed">Completed</label>
                            <input type="checkbox" id="online_assessment_completed" v-model="type_a.online_assessment_completed">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="digital_interview_date">Digital Interview Date</label>
                        <input type="date" class="form-control" id="digital_interview_date" v-model="type_a.digital_interview_date">
                        <div class="input-container-2">
                            <label for="digital_interview_completed">Completed</label>
                            <input type="checkbox" id="digital_interview_completed" v-model="type_a.digital_interview_completed">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="assessment_centre_date">Assessment Centre Date</label>
                        <input type="date" class="form-control" id="assessment_centre_date" v-model="type_a.assessment_centre_date">
                        <div class="input-container-2">
                            <label for="assessment_centre_completed">Completed</label>
                            <input type="checkbox" id="assessment_centre_completed" v-model="type_a.assessment_centre_completed">
                        </div>
                    </div>
                </div>

                <!-- TypeB-specific fields -->
                <div v-if="application_type === 'B'">
                    <div class="form-group">
                        <label for="recruiter_interview_date">Recruiter Interview Date</label>
                        <input type="date" class="form-control" id="recruiter_interview_date" v-model="type_b.recruiter_interview_date">
                        <div class="input-container-2">
                            <label for="recruiter_interview_completed">Completed</label>
                            <input type="checkbox" id="recruiter_interview_completed" v-model="type_b.recruiter_interview_completed">
                        </div> 
                    </div>
                    <div class="form-group">
                        <label for="technical_interview_date">Technical Interview Date</label>
                        <input type="date" class="form-control" id="technical_interview_date" v-model="type_b.technical_interview_date">
                        <div class="input-container-2">
                            <label for="technical_interview_completed">Completed</label>
                            <input type="checkbox" id="technical_interview_completed" v-model="type_b.technical_interview_completed">
                        </div>   
                    </div>
                    <div class="form-group">
                        <label for="behavioural_interview_date">Behavioural Interview Date</label>
                        <input type="date" class="form-control" id="behavioural_interview_date" v-model="type_b.behavioural_interview_date">
                        <div class="input-container-2">
                            <label for="behavioural_interview_completed">Completed</label>
                            <input type="checkbox" id="behavioural_interview_completed" v-model="type_b.behavioural_interview_completed">
                        </div> 
                    </div>
                </div>

                <div class="form-group" id="submit-button-group">
                    <button type="submit">Add Job Application</button>
                    <button @click="closeForm">Cancel</button>
                </div>
            </div>
        </form>
    </div>
    
    <div class="modal-overlay">
        <div v-if="showModal" class="modal">
            <div class="modal-content">
                
                <div class="form-group">
                    <label for="company_name">Company Name</label>
                    <input type="text" class="form-control" id="edit_company_name" v-model="editingJob.company_name">
                </div>
                <div class="form-group">
                    <label for="role_position">Role/Position</label>
                    <input type="text" class="form-control" id="edit_role_position" v-model="editingJob.role_position">
                </div>
                <div class="form-group">
                    <label for="initial_application_submission_date">Submission Date</label>
                    <input type="date" class="form-control" id="edit_initial_application_submission_date" v-model="editingJob.initial_application_submission_date">
                </div>
                <div class="form-group">
                    <label for="edit_application_type">Application Type</label>
                    <select id="edit_application_type" v-model="editingJob.application_type">
                        <option value="A">Type A Process</option>
                        <option value="B">Type B Process</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="edit_result">Result</label>
                    <select id="edit_result" v-model="editingJob.result">
                        <option value="Waiting">Waiting</option>
                        <option value="Offer">Offer</option>
                        <option value="Rejected">Rejected</option>
                    </select>
                </div>
                <!-- TypeA-specific fields -->
                <div v-if="editingJob.application_type === 'A'">
                    <div class="form-group">
                        <label for="online_assessment_date">Online Assessment Date</label>
                        <input type="date" class="form-control" id="edit_online_assessment_date" v-model="editingJob.type_a.online_assessment_date">
                        <div class="input-container-2">
                            <label for="online_assessment_completed">Completed</label>
                            <input type="checkbox" id="edit_online_assessment_completed" v-model="editingJob.type_a.online_assessment_completed">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="digital_interview_date">Digital Interview Date</label>
                        <input type="date" class="form-control" id="edit_digital_interview_date" v-model="editingJob.type_a.digital_interview_date">
                        <div class="input-container-2">
                            <label for="digital_interview_completed">Completed</label>
                            <input type="checkbox" id="digital_interview_completed" v-model="editingJob.type_a.digital_interview_completed">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="assessment_centre_date">Assessment Centre Date</label>
                        <input type="date" class="form-control" id="edit_assessment_centre_date" v-model="editingJob.type_a.assessment_centre_date">
                        <div class="input-container-2">
                            <label for="assessment_centre_completed">Completed</label>
                            <input type="checkbox" id="edit_assessment_centre_completed" v-model="editingJob.type_a.assessment_centre_completed">
                        </div>  
                    </div>
                </div>

                <!-- TypeB-specific fields -->
                <div v-if="editingJob.application_type === 'B'">
                    <div class="form-group">
                        <label for="recruiter_interview_date">Recruiter Interview Date</label>
                        <input type="date" class="form-control" id="edit_recruiter_interview_date" v-model="editingJob.type_b.recruiter_interview_date">
                        <div class="input-container-2">
                            <label for="recruiter_interview_completed">Completed</label>
                            <input type="checkbox" id="edit_recruiter_interview_completed" v-model="editingJob.type_b.recruiter_interview_completed">
                        </div>  
                    </div>
                    <div class="form-group">
                        <label for="technical_interview_date">Technical Interview Date</label>
                        <input type="date" class="form-control" id="edit_technical_interview_date" v-model="editingJob.type_b.technical_interview_date">
                        <div class="input-container-2">
                            <label for="technical_interview_completed">Completed</label>
                            <input type="checkbox" id="edit_technical_interview_completed" v-model="editingJob.type_b.technical_interview_completed">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="behavioural_interview_date">Behavioural Interview Date</label>
                        <input type="date" class="form-control" id="edit_behavioural_interview_date" v-model="editingJob.type_b.behavioural_interview_date">
                        <div class="input-container-2">
                            <label for="behavioural_interview_completed">Completed</label>
                            <input type="checkbox" id="edit_behavioural_interview_completed" v-model="editingJob.type_b.behavioural_interview_completed">
                        </div>  
                    </div>
                </div>

                <div class="action-button-group">
                    <button type="button" class="primary-btn" @click="saveChanges">Save Changes</button>
                    <button class="secondary-btn" @click="closeModal">Cancel</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
export default {
    data() {
        return {
            jobs: [],
            company_name: '',
            role_position: '',
            initial_application_submission_date: '',
            application_type: '',
            result: '',
            type_a: {
                online_assessment_date: '',
                online_assessment_completed: false,
                digital_interview_date: '',
                digital_interview_completed: false,
                assessment_centre_date: '',
                assessment_centre_completed: false
            },
            type_b: {
                recruiter_interview_date: '',
                recruiter_interview_completed: false,
                technical_interview_date: '',
                technical_interview_completed: false,
                behavioural_interview_date: '',
                behavioural_interview_completed: false
            },
            showModal: false,
            showForm: false,
            editingJob: null,
            sortKey: '',
            sortDirection: 1,
            searchTerm: '',
        };
    },
    computed: {
        sortedJobs() {           // added for sorting
            return this.jobs.sort((a, b) => {
                if (a[this.sortKey] < b[this.sortKey]) return -1 * this.sortDirection;
                if (a[this.sortKey] > b[this.sortKey]) return 1 * this.sortDirection;
                return 0;
            });
        },
        filteredJobs() {
            if (!this.searchTerm) return this.sortedJobs;

            return this.sortedJobs.filter(job => 
                job.company_name.toLowerCase().includes(this.searchTerm.toLowerCase())
            );
        }
        
    },
    methods: {
        async getData() {
            try {
                const response = await this.$http.get('http://localhost:8000/jobs/jobs/');
                this.jobs = response.data;
                console.log("Jobs Data:", this.jobs);  // log the data
            } catch (error) {
                console.log(error);
            }
        },
        sortTable(key) {
            // Handle previous key logic
            if (this.sortKey === key) {
                this.sortDirection *= -1;
            } else {
                this.sortKey = key;
                this.sortDirection = 1;
            }

            // Sorting based on key
            this.jobs.sort((a, b) => {
                let dateA, dateB, completedA, completedB;
                
                switch (key) {
                    case 'Round 1':
                        dateA = a.application_type === 'A' ? a.type_a.online_assessment_date : a.type_b.recruiter_interview_date;
                        dateB = b.application_type === 'A' ? b.type_a.online_assessment_date : b.type_b.recruiter_interview_date;
                        completedA = a.application_type === 'A' ? a.type_a.online_assessment_completed : a.type_b.recruiter_interview_completed;
                        completedB = b.application_type === 'A' ? b.type_a.online_assessment_completed : b.type_b.recruiter_interview_completed;
                        break;
                    case 'Round 2':
                        dateA = a.application_type === 'A' ? a.type_a.digital_interview_date : a.type_b.technical_interview_date;
                        dateB = b.application_type === 'A' ? b.type_a.digital_interview_date : b.type_b.technical_interview_date;
                        completedA = a.application_type === 'A' ? a.type_a.digital_interview_completed : a.type_b.technical_interview_completed;
                        completedB = b.application_type === 'A' ? b.type_a.digital_interview_completed : b.type_b.technical_interview_completed;
                        break;
                    case 'Round 3':
                        dateA = a.application_type === 'A' ? a.type_a.assessment_centre_date : a.type_b.behavioural_interview_date;
                        dateB = b.application_type === 'A' ? b.type_a.assessment_centre_date : b.type_b.behavioural_interview_date;
                        completedA = a.application_type === 'A' ? a.type_a.assessment_centre_completed : a.type_b.behavioural_interview_completed;
                        completedB = b.application_type === 'A' ? b.type_a.assessment_centre_completed : b.type_b.behavioural_interview_completed;
                        break;
                    default:
                        // for other columns, including company_name, role_position, etc.
                        dateA = a[key];
                        dateB = b[key];
                }

                // Comparison for date
                if (dateA < dateB) return -1 * this.sortDirection;
                if (dateA > dateB) return 1 * this.sortDirection;
                
                // Comparison for completion status if dates are identical (and if it's one of the Round columns)
                if (['Round 1', 'Round 2', 'Round 3'].includes(key)) {
                    if (completedA && !completedB) return -1 * this.sortDirection;
                    if (!completedA && completedB) return 1 * this.sortDirection;
                }
                
                return 0;
            });
        },
        async submitForm(){
            try {
                // Prepare the job application data
                const jobApplicationData = {
                    company_name: this.company_name,
                    role_position: this.role_position,
                    initial_application_submission_date: this.initial_application_submission_date,
                    application_type: this.application_type,
                    result: this.result,
                    type_a: this.application_type === 'A' ? {
                        online_assessment_date: this.type_a.online_assessment_date || null,
                        online_assessment_completed: this.type_a.online_assessment_completed,
                        digital_interview_date: this.type_a.digital_interview_date || null,
                        digital_interview_completed: this.type_a.digital_interview_completed,
                        assessment_centre_date: this.type_a.assessment_centre_date || null,
                        assessment_centre_completed: this.type_a.assessment_centre_completed,
                    } : null,
                        type_b: this.application_type === 'B' ? {
                        recruiter_interview_date: this.type_b.recruiter_interview_date || null,
                        recruiter_interview_completed: this.type_b.recruiter_interview_completed,
                        technical_interview_date: this.type_b.technical_interview_date || null,
                        technical_interview_completed: this.type_b.technical_interview_completed,
                        behavioural_interview_date: this.type_b.behavioural_interview_date || null,
                        behavioural_interview_completed: this.type_b.behavioural_interview_completed,
                    } : null,

                };

                // Send a POST request to the API
                const response = await this.$http.post('http://localhost:8000/jobs/jobs/', jobApplicationData);
                
                // Append the returned data to the jobs array
                this.jobs.push(response.data);

                // Reset the form fields
                this.company_name = '';
                this.role_position = '';
                this.initial_application_submission_date = '';
                this.application_type = '';
                this.result = '';
                this.type_a = {
                    online_assessment_date: '',
                    online_assessment_completed: false,
                    digital_interview_date: '',
                    digital_interview_completed: false,
                    assessment_centre_date: '',
                    assessment_centre_completed: false
                };
                this.type_b = {
                    recruiter_interview_date: '',
                    recruiter_interview_completed: false,
                    technical_interview_date: '',
                    technical_interview_completed: false,
                    behavioural_interview_date: '',
                    behavioural_interview_completed: false
                };

                this.closeForm();
            } catch (error) {
                // Log the error
                console.log(error);
            }
        },
        async deleteJob(job){

        // Confirm if one wants to delete the task
            let confirmation = confirm("Do you want to delete this job?"); 

            if(confirmation){
                try{

                // Send a request to delete the task
                await this.$http.delete(`http://localhost:8000/jobs/jobs/${job.id}/`);

                // Refresh the tasks
                this.getData();
                }catch(error){
                // Log any error

                console.log(error)
                }
            }      
        },
        editJob(job) {
            this.editingJob = { ...job };
            this.showModal = true;
        },
        addJob() {
            this.showForm = true;
        },
        async saveChanges() {
            try {
                console.log('Editing Job:', this.editingJob); // Log the editing object
                const response = await this.$http.put(`http://localhost:8000/jobs/jobs/${this.editingJob.id}/`, this.editingJob);
                // Refresh the jobs
                this.getData();
                this.showModal = false;
            } catch (error) {
                console.log(error);
            }
        },
        closeModal() {
            this.showModal = false;
        },
        closeForm() {
            this.showForm = false;
        },
        getResultClass(result) {
            switch (result) {
                case 'Waiting':
                    return 'result-waiting';
                case 'Offer':
                    return 'result-offer';
                case 'Rejected':
                    return 'result-rejected';
                default:
                    return '';  // Default class, if needed
            }
        },
    },
    created() {
            this.getData();
    }
}
</script>

<style>
.modal, .add_job {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.addjob_button {
    background-color: #007BFF; /* A deep blue color, commonly used for primary actions */
    color: #ffffff;            /* White text color */
    padding: 10px 20px;        /* Padding to give the button some space */
    border: none;              /* Remove any default borders */
    border-radius: 5px;        /* Slight rounded corners */
    font-size: 16px;           /* A bigger font size */
    cursor: pointer;           /* A pointer cursor when hovering over the button */
    transition: background-color 0.3s ease; /* A transition for smooth hover effect */
    box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1); /* A subtle box shadow for depth */
    outline: none;             /* Remove the outline that appears when the button is clicked */
    text-align: center;        /* Center the text within the button */
    display: inline-block;     /* Allow for text-align to work */
    margin-bottom: 1%;
}

.addjob_button:hover {
    background-color: #0056b3; /* A slightly darker blue for hover */
}

.addjob_button:active {
    background-color: #003d7a; /* Even darker blue for when the button is actively being clicked */
    box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.1); /* Decrease the shadow to give a "pushed" effect */
}


.modal-content, .form-content {
    background-color: #ffffff;
    max-width: 500px;
    padding: 20px 40px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}

.form-group {
    margin-bottom: 10%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.form-group > input {
    border: 1px solid #ccc;
    padding: 5px 50px;
    width: 60%;
}

.form-group > select {
    border: 1px solid #ccc;
    padding: 5px 50px;
    width: 100%;
}

.form-group > label {
    margin-bottom: 3%;
}

.form-group > .input-container-2 {
    display: flex;            /* This will make the child elements sit side by side */
    align-items: center;      /* Vertically center align the child elements */
    gap: 10px;                /* Add space between child elements */
}

.form-control {
    flex: 1;                  /* This will make the date input take up the remaining space */
}

.buttons-container {
    display: flex;
    flex-direction: column;
    gap: 10px; /* Optional: adds a gap between the buttons */
}

.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.check {
    color: green;
}
.cross {
    color: red;
}

table {
    width: 80%;
    border-collapse: collapse;
    margin: auto;
    font-size: 0.9em;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

th, td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid #ddd;
    text-align: center; /* centers content horizontally */
    vertical-align: middle; /* centers content vertically */
}

th {
    background-color: #2C3E50;
    color: white;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

tr:hover {
    background-color: #f5f5f5;
    cursor: pointer;
}

tr:last-of-type {
    border-bottom: 2px solid #2C3E50;
}

/* Icons and their colors */

.check {
    color: green;
    font-weight: bold;
    font-size: 1.2em;
}

.cross {
    color: red;
    font-weight: bold;
    font-size: 1.2em;
}

/* Styling for the buttons */

.buttons-container {
    display: flex;
    gap: 10px;
    justify-content: center; /* horizontal centering for flex items */
    align-items: center; /* vertical centering for flex items */
}

.buttons-container > button {
    padding: 5px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.buttons-container > button:hover {
    opacity: 0.9;
}

.buttons-container > button:nth-child(1) {
    background-color: #2980B9; /* Blue */
    color: white;
}

.buttons-container > button:nth-child(2) {
    background-color: #E74C3C; /* Red */
    color: white;
}

/* Form Group Styling */
#submit-button-group {
    display: flex;            /* Layout the buttons side by side */
    justify-content: space-between; /* Space them out evenly */
    gap: 10px;                /* Gap between buttons */
    margin-top: 20px;         /* Optional top margin for spacing */
}

/* Primary Button Styling (Add Job Application) */
#submit-button-group button[type="submit"] {
    background-color: #007BFF; /* A deep blue color for primary actions */
    color: #ffffff;            /* White text color */
    padding: 10px 20px;        /* Padding for space */
    border: none;              /* Remove default borders */
    border-radius: 5px;        /* Rounded corners */
    font-size: 16px;           /* Font size */
    cursor: pointer;           /* Pointer cursor for hover */
    transition: background-color 0.3s ease; /* Smooth hover transition */
    box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1); /* Subtle box shadow for depth */
    outline: none;             /* Remove the click outline */
}

/* Hover effect for the Primary Button */
#submit-button-group button[type="submit"]:hover {
    background-color: #0056b3; /* Darker blue on hover */
}

/* Active (click) effect for the Primary Button */
#submit-button-group button[type="submit"]:active {
    background-color: #003d7a; /* Even darker blue on click */
    box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.1); /* "Pushed" shadow effect */
}

/* Secondary Button Styling (Cancel) */
#submit-button-group button:not([type="submit"]) {
    background-color: #f4f4f4; /* A light gray background */
    color: #333;               /* Dark gray text color */
    padding: 10px 20px;        /* Padding for space */
    border: 1px solid #ccc;    /* Slight border for definition */
    border-radius: 5px;        /* Rounded corners */
    font-size: 16px;           /* Font size */
    cursor: pointer;           /* Pointer cursor for hover */
    transition: background-color 0.3s ease, color 0.3s ease; /* Smooth hover transition */
    outline: none;             /* Remove the click outline */
}

/* Hover effect for the Secondary Button */
#submit-button-group button:not([type="submit"]):hover {
    background-color: #e0e0e0; /* Darker gray on hover */
}

/* Active (click) effect for the Secondary Button */
#submit-button-group button:not([type="submit"]):active {
    background-color: #bfbfbf; /* Even darker gray on click */
}

/* General Button Group Styling */
.action-button-group {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    margin-top: 20px;
}

/* Primary Button Styling */
.primary-btn {
    background-color: #007BFF;
    color: #ffffff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);
    outline: none;
}

.primary-btn:hover {
    background-color: #0056b3;
}

.primary-btn:active {
    background-color: #003d7a;
    box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.1);
}

/* Secondary Button Styling */
.secondary-btn {
    background-color: #f4f4f4;
    color: #333;
    padding: 10px 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease, color 0.3s ease;
    outline: none;
}

.secondary-btn:hover {
    background-color: #e0e0e0;
}

.secondary-btn:active {
    background-color: #bfbfbf;
}

/* Result colors */
.result-waiting {
    color: #FFA500; /* Orange for "Waiting" */
}

.result-offer {
    color: #32CD32; /* LimeGreen for "Offer" */
}

.result-rejected {
    color: #FF0000; /* Red for "Rejected" */
}

.searchbar {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 20px; /* Space between search and table */
    width: 10%; /* Full width */
}

</style>