package com.changeapp.domain;

import org.hibernate.annotations.Cache;
import org.hibernate.annotations.CacheConcurrencyStrategy;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Objects;

/**
 * A TaskStructureConfig.
 */
@Entity
@Table(name = "task_structure_config")
@Cache(usage = CacheConcurrencyStrategy.NONSTRICT_READ_WRITE)
public class TaskStructureConfig implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "parent_id")
    private Integer parentID;

    @Column(name = "sort_in_parent_id")
    private String sortInParentID;

    @Column(name = "name")
    private String name;

    @Column(name = "jhi_type")
    private String type;

    @Column(name = "question_type")
    private String questionType;

    @Column(name = "question_answer_list_id")
    private Integer questionAnswerListID;

    @Column(name = "people_role")
    private Integer peopleRole;

    @Column(name = "jhi_order")
    private Integer order;

    @ManyToOne
    private RequestTypeDefConfig requestTypeDefConfig;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Integer getParentID() {
        return parentID;
    }

    public TaskStructureConfig parentID(Integer parentID) {
        this.parentID = parentID;
        return this;
    }

    public void setParentID(Integer parentID) {
        this.parentID = parentID;
    }

    public String getSortInParentID() {
        return sortInParentID;
    }

    public TaskStructureConfig sortInParentID(String sortInParentID) {
        this.sortInParentID = sortInParentID;
        return this;
    }

    public void setSortInParentID(String sortInParentID) {
        this.sortInParentID = sortInParentID;
    }

    public String getName() {
        return name;
    }

    public TaskStructureConfig name(String name) {
        this.name = name;
        return this;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getType() {
        return type;
    }

    public TaskStructureConfig type(String type) {
        this.type = type;
        return this;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getQuestionType() {
        return questionType;
    }

    public TaskStructureConfig questionType(String questionType) {
        this.questionType = questionType;
        return this;
    }

    public void setQuestionType(String questionType) {
        this.questionType = questionType;
    }

    public Integer getQuestionAnswerListID() {
        return questionAnswerListID;
    }

    public TaskStructureConfig questionAnswerListID(Integer questionAnswerListID) {
        this.questionAnswerListID = questionAnswerListID;
        return this;
    }

    public void setQuestionAnswerListID(Integer questionAnswerListID) {
        this.questionAnswerListID = questionAnswerListID;
    }

    public Integer getPeopleRole() {
        return peopleRole;
    }

    public TaskStructureConfig peopleRole(Integer peopleRole) {
        this.peopleRole = peopleRole;
        return this;
    }

    public void setPeopleRole(Integer peopleRole) {
        this.peopleRole = peopleRole;
    }

    public Integer getOrder() {
        return order;
    }

    public TaskStructureConfig order(Integer order) {
        this.order = order;
        return this;
    }

    public void setOrder(Integer order) {
        this.order = order;
    }

    public RequestTypeDefConfig getRequestTypeDefConfig() {
        return requestTypeDefConfig;
    }

    public TaskStructureConfig requestTypeDefConfig(RequestTypeDefConfig requestTypeDefConfig) {
        this.requestTypeDefConfig = requestTypeDefConfig;
        return this;
    }

    public void setRequestTypeDefConfig(RequestTypeDefConfig requestTypeDefConfig) {
        this.requestTypeDefConfig = requestTypeDefConfig;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        TaskStructureConfig taskStructureConfig = (TaskStructureConfig) o;
        if (taskStructureConfig.getId() == null || getId() == null) {
            return false;
        }
        return Objects.equals(getId(), taskStructureConfig.getId());
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(getId());
    }

    @Override
    public String toString() {
        return "TaskStructureConfig{" +
            "id=" + getId() +
            ", parentID='" + getParentID() + "'" +
            ", sortInParentID='" + getSortInParentID() + "'" +
            ", name='" + getName() + "'" +
            ", type='" + getType() + "'" +
            ", questionType='" + getQuestionType() + "'" +
            ", questionAnswerListID='" + getQuestionAnswerListID() + "'" +
            ", peopleRole='" + getPeopleRole() + "'" +
            ", order='" + getOrder() + "'" +
            "}";
    }
}
