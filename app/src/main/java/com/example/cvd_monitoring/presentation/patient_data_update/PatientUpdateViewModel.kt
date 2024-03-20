package com.example.cvd_monitoring.presentation.patient_data_update

import android.util.Log
import androidx.compose.runtime.State
import androidx.compose.runtime.mutableStateOf
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.cvd_monitoring.common.TextFieldState
import com.example.cvd_monitoring.domain.model.users.PatientData
import com.example.cvd_monitoring.domain.use_case.current_user.CurrentUserUseCase
import com.example.cvd_monitoring.domain.use_case.patient_data.PatientDataUseCase
import com.example.cvd_monitoring.presentation.CurrentUserState
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class PatientUpdateViewModel @Inject constructor(
    private val patientDataUseCase: PatientDataUseCase,
    private val currentUserUseCase: CurrentUserUseCase,
) : ViewModel() {
    private val _ageState = mutableStateOf(TextFieldState())
    val ageState: State<TextFieldState> = _ageState

    fun setAgeValue(value: String) {
        _ageState.value = ageState.value.copy(text = value)
    }

    private val _heightState = mutableStateOf(TextFieldState())
    val heightState: State<TextFieldState> = _heightState

    fun setHeightValue(value: String) {
        _heightState.value = heightState.value.copy(text = value)
    }

    private val _weightState = mutableStateOf(TextFieldState())
    val weightState: State<TextFieldState> = _weightState

    fun setWeightValue(value: String) {
        _weightState.value = weightState.value.copy(text = value)
    }

    private val _genderState = mutableStateOf(TextFieldState())
    val genderState: State<TextFieldState> = _genderState

    fun setGenderValue(value: String) {
        _genderState.value = genderState.value.copy(text = value)
    }

    private val _birthdayState = mutableStateOf(TextFieldState())
    val birthdayState: State<TextFieldState> = _birthdayState

    fun setBirthdayValue(value: String) {
        _birthdayState.value = birthdayState.value.copy(text = value)
    }

    private val _state = mutableStateOf(CurrentUserState())
    val state: State<CurrentUserState> = _state

    fun getCurrentUser(slug: String) {
        viewModelScope.launch {
            try {
                val currentUser = currentUserUseCase(slug)
                _state.value = CurrentUserState(currentUser)
                state.value.patient?.let { setAgeValue(it.age.toString()) }
                state.value.patient?.let { setHeightValue(it.height.toString()) }
                state.value.patient?.let { setWeightValue(it.weight.toString()) }
                state.value.patient?.let { setGenderValue(it.gender) }
                state.value.patient?.let { setBirthdayValue(it.birthday) }
            } catch (e: Exception) {
                val errorMessage = e.message.toString()
                Log.e("PatientListViewModel", errorMessage, e)
            }
        }
    }


    fun updatePatientData(slug: String) {
        val age = ageState.value.text
        val height = heightState.value.text
        val weight = weightState.value.text
        val gender = genderState.value.text
        val birthday = birthdayState.value.text

        viewModelScope.launch {
            try {
                val patientData  = PatientData(age.toInt(), birthday, gender, height.toInt(), weight.toDouble())
                val createdUser = patientDataUseCase(patientData, slug)
                Log.d("SignUpViewModel", "Sign up successful: $createdUser")
            } catch (e: Exception) {
                val errorMessage = e.message.toString()
                Log.e("SignUpViewModel", "Sign up error: $errorMessage", e)
            }
        }
    }
}