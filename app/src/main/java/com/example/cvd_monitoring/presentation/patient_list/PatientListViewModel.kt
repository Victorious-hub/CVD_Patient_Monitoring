package com.example.cvd_monitoring.presentation.patient_list

import android.util.Log
import androidx.compose.runtime.mutableStateOf
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.domain.use_case.patient_list.GetPatientListUseCase
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class PatientListViewModel @Inject constructor(
    private val getPatientListUseCase: GetPatientListUseCase
) : ViewModel() {
    private val _patientListResponse = MutableStateFlow(emptyList<Patient>())
    val patientListResponse: StateFlow<List<Patient>> = _patientListResponse

    private val _errorMessage = mutableStateOf("")
    val errorMessage: String = _errorMessage.value

    private val _isLoading = mutableStateOf(false)
    val isLoading: Boolean = _isLoading.value

    init {
        getPatientList()
    }

    private fun getPatientList() {
        viewModelScope.launch {
            try {
                _isLoading.value = true
                val patientList = getPatientListUseCase()
                _patientListResponse.value = patientList
                Log.d("PatientListViewModel", "Patient list fetched: $patientList")
            } catch (e: Exception) {
                _errorMessage.value = e.message.toString()
                Log.e("PatientListViewModel", "Failed to fetch patient list", e)
            } finally {
                _isLoading.value = false
            }
        }
    }
}