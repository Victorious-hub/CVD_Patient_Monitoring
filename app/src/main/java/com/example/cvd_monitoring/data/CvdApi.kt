package com.example.cvd_monitoring.data

import com.example.cvd_monitoring.domain.model.users.Auth
import com.example.cvd_monitoring.domain.model.users.CreateUserRequest
import com.example.cvd_monitoring.domain.model.users.Doctor
import com.example.cvd_monitoring.domain.model.users.DoctorContact
import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.domain.model.users.PatientContact
import com.example.cvd_monitoring.domain.model.users.PatientData
import com.example.cvd_monitoring.domain.model.users.User
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.PATCH
import retrofit2.http.POST
import retrofit2.http.PUT
import retrofit2.http.Path

interface CvdApi {
    @POST("users/v1/patients/registration")
    suspend fun createPatient(@Body patient: CreateUserRequest): User

    @GET("users/v1/patients")
    suspend fun getPatients(): List<Patient>
    @POST("auth/v1/authenticate")
    suspend fun authenticateUser(@Body auth: Auth): Auth
    @PUT("users/v1/patients/update/{slug}/data")
    suspend fun updatePatientData(@Body patient: PatientData, @Path("slug") slug: String): PatientData
    @PUT("users/v1/patients/update/{slug}/contact")
    suspend fun updatePatientContact(@Body patient: PatientContact, @Path("slug") slug: String): PatientContact
    @GET("users/v1/patients/{slug}/get")
    suspend fun getCurrentUser(@Path("slug") slug: String): Patient
    @PUT("users/v1/doctors/{slug/contact")
    suspend fun updateDoctorContact(@Body doctor: DoctorContact, @Path("slug") slug: String): DoctorContact

}