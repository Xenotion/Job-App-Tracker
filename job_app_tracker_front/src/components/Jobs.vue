<!-- eslint-disable -->

<template>
    <div class="jobs_container">
        <div class="jobs_content">
            <h1>Job Applications</h1>
            <button @click="addJob()">Add Job</button>
            <div class="header">
                <h2>Company</h2>
                <h2>Role</h2>
                <h2>Application Date</h2>
                <h2>Assessment Date</h2>
                <h2>Result</h2>
                <h2>Edit</h2>
            </div>
            <ul class="jobs_list">
                <li v-for="job in jobs" :key="job.id">
                    <h2>{{ job.company_name }}</h2>
                    <p>{{ job.role_position }}</p>
                    <p>{{ job.initial_application_submission_date }}</p>

                    <div v-if="job.application_type === 'A' && job.type_a">
                        <div class="info-row">
                            <p>Online Assessment Date: {{ job.type_a.online_assessment_date }}</p>
                            <p :class="job.type_a.online_assessment_completed ? 'check' : 'cross'">{{ job.type_a.online_assessment_completed ? '✔️' : '❌' }}</p>
                        </div>
                        <div class="info-row">
                            <p>Digital Interview Date: {{ job.type_a.digital_interview_date }}</p>
                            <p :class="job.type_a.digital_interview_completed ? 'check' : 'cross'">{{ job.type_a.digital_interview_completed ? '✔️' : '❌' }}</p>
                        </div>
                        <div class="info-row">
                            <p>Assessment Centre Date: {{ job.type_a.assessment_centre_date }}</p>
                            <p :class="job.type_a.assessment_centre_completed ? 'check' : 'cross'">{{ job.type_a.assessment_centre_completed ? '✔️' : '❌' }}</p>
                        </div>
                    </div>

                    <div v-if="job.application_type === 'B' && job.type_b">
                        <div class="info-row">
                            <p>Recruiter Interview Date: {{ job.type_b.recruiter_interview_date }}</p>
                            <p :class="job.type_b.recruiter_interview_completed ? 'check' : 'cross'">{{ job.type_b.recruiter_interview_completed ? '✔️' : '❌' }}</p>
                        </div>
                        <div class="info-row">
                            <p>Technical Interview Date: {{ job.type_b.technical_interview_date }}</p>
                            <p :class="job.type_b.technical_interview_completed ? 'check' : 'cross'">{{ job.type_b.technical_interview_completed ? '✔️' : '❌' }}</p>
                        </div>
                        <div class="info-row">
                            <p>Behavioural Interview Date: {{ job.type_b.behavioural_interview_date }}</p>
                            <p :class="job.type_b.behavioural_interview_completed ? 'check' : 'cross'">{{ job.type_b.behavioural_interview_completed ? '✔️' : '❌' }}</p>
                        </div>
                    </div>

                    <p>{{ job.result }}</p>

                    <button @click="editJob(job)">Update</button>
                    <button @click="deleteJob(job)">Delete</button>
                </li>
            </ul>
        </div>
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
                        <input type="checkbox" id="online_assessment_completed" v-model="type_a.online_assessment_completed">
                        <label for="online_assessment_completed">Completed</label>
                    </div>
                    <div class="form-group">
                        <label for="digital_interview_date">Digital Interview Date</label>
                        <input type="date" class="form-control" id="digital_interview_date" v-model="type_a.digital_interview_date">
                        <input type="checkbox" id="digital_interview_completed" v-model="type_a.digital_interview_completed">
                        <label for="digital_interview_completed">Completed</label>
                    </div>
                    <div class="form-group">
                        <label for="assessment_centre_date">Assessment Centre Date</label>
                        <input type="date" class="form-control" id="assessment_centre_date" v-model="type_a.assessment_centre_date">
                        <input type="checkbox" id="assessment_centre_completed" v-model="type_a.assessment_centre_completed">
                        <label for="assessment_centre_completed">Completed</label>
                    </div>
                </div>

                <!-- TypeB-specific fields -->
                <div v-if="application_type === 'B'">
                    <div class="form-group">
                        <label for="recruiter_interview_date">Recruiter Interview Date</label>
                        <input type="date" class="form-control" id="recruiter_interview_date" v-model="type_b.recruiter_interview_date">
                        <input type="checkbox" id="recruiter_interview_completed" v-model="type_b.recruiter_interview_completed">
                        <label for="recruiter_interview_completed">Completed</label>
                    </div>
                    <div class="form-group">
                        <label for="technical_interview_date">Technical Interview Date</label>
                        <input type="date" class="form-control" id="technical_interview_date" v-model="type_b.technical_interview_date">
                        <input type="checkbox" id="technical_interview_completed" v-model="type_b.technical_interview_completed">
                        <label for="technical_interview_completed">Completed</label>
                    </div>
                    <div class="form-group">
                        <label for="behavioural_interview_date">Behavioural Interview Date</label>
                        <input type="date" class="form-control" id="behavioural_interview_date" v-model="type_b.behavioural_interview_date">
                        <input type="checkbox" id="behavioural_interview_completed" v-model="type_b.behavioural_interview_completed">
                        <label for="behavioural_interview_completed">Completed</label>
                    </div>
                </div>

                <div class="form-group">
                    <button type="submit">Add Job Application</button>
                    <button @click="closeForm">Cancel</button>
                </div>
            </div>
        </form>
    </div>
    
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
                    <input type="checkbox" id="edit_online_assessment_completed" v-model="editingJob.type_a.online_assessment_completed">
                    <label for="online_assessment_completed">Completed</label>
                </div>
                <div class="form-group">
                    <label for="digital_interview_date">Digital Interview Date</label>
                    <input type="date" class="form-control" id="edit_digital_interview_date" v-model="editingJob.type_a.digital_interview_date">
                    <input type="checkbox" id="digital_interview_completed" v-model="editingJob.type_a.digital_interview_completed">
                    <label for="digital_interview_completed">Completed</label>
                </div>
                <div class="form-group">
                    <label for="assessment_centre_date">Assessment Centre Date</label>
                    <input type="date" class="form-control" id="edit_assessment_centre_date" v-model="editingJob.type_a.assessment_centre_date">
                    <input type="checkbox" id="edit_assessment_centre_completed" v-model="editingJob.type_a.assessment_centre_completed">
                    <label for="assessment_centre_completed">Completed</label>
                </div>
            </div>

            <!-- TypeB-specific fields -->
            <div v-if="editingJob.application_type === 'B'">
                <div class="form-group">
                    <label for="recruiter_interview_date">Recruiter Interview Date</label>
                    <input type="date" class="form-control" id="edit_recruiter_interview_date" v-model="editingJob.type_b.recruiter_interview_date">
                    <input type="checkbox" id="edit_recruiter_interview_completed" v-model="editingJob.type_b.recruiter_interview_completed">
                    <label for="recruiter_interview_completed">Completed</label>
                </div>
                <div class="form-group">
                    <label for="technical_interview_date">Technical Interview Date</label>
                    <input type="date" class="form-control" id="edit_technical_interview_date" v-model="editingJob.type_b.technical_interview_date">
                    <input type="checkbox" id="edit_technical_interview_completed" v-model="editingJob.type_b.technical_interview_completed">
                    <label for="technical_interview_completed">Completed</label>
                </div>
                <div class="form-group">
                    <label for="behavioural_interview_date">Behavioural Interview Date</label>
                    <input type="date" class="form-control" id="edit_behavioural_interview_date" v-model="editingJob.type_b.behavioural_interview_date">
                    <input type="checkbox" id="edit_behavioural_interview_completed" v-model="editingJob.type_b.behavioural_interview_completed">
                    <label for="behavioural_interview_completed">Completed</label>
                </div>
            </div>


            <button type="button" @click="saveChanges">Save Changes</button>
            <button @click="closeModal">Cancel</button>
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
            };
        },
        methods: {
            async getData() {
                try {
                    const response = await this.$http.get('http://localhost:8000/jobs/jobs/');
                    // set the data returned as jobs
                    this.jobs = response.data; 
                } catch (error) {
                    // log the error
                    console.log(error);
                }
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
            }
        },
        created() {
            // Fetch jobs on page load
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

.modal-content, .form-content {
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
}

.header {
    display: flex;
    flex-wrap: wrap;
    /* justify-self: space-between; */
    align-items: center;
    padding: 15px;
    margin: auto;
    
}

.jobs_list {
    list-style-type: none;
    padding: 0;
    margin: 20px;
}

.jobs_list li {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    background-color: #f5f5f5;
}

.jobs_list h2, .jobs_list h3, .jobs_list p {
    margin: 5px;
}

.jobs_list h2 {
    font-size: 1.25em;
    color: #333;
}

.jobs_list h3 {
    font-size: 1.1em;
    color: #666;
}

.jobs_list p {
    font-size: 0.9em;
    color: #444;
}

.jobs_list button {
    background-color: #4285f4;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-right: 10px;
}

.jobs_list button:hover {
    background-color: #357abd;
}

.jobs_list button:last-child {
    background-color: #d9534f;
}

.jobs_list button:last-child:hover {
    background-color: #c9302c;
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

</style>